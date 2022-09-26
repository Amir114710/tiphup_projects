from django.shortcuts import render , redirect
from django.urls import reverse , reverse_lazy
from .form import LoginForm , SignupForm , Edite_Profile_Form
from django.views.generic import FormView , TemplateView , CreateView
from django.contrib.auth import authenticate, login , logout
from .models import User
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes , force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from mixins import LoginRequirdMixins , LogoutRequirdMixins
from blog.models import Notification
class LoginFormView(LoginRequirdMixins , FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')
    def form_valid(self, form):
        context = {'errors' : []}
        cd = form.cleaned_data
        user = authenticate(self.request , username = cd['username'] , password = cd['password'])
        if user is not None:
            login(self.request , user)
            return redirect(reverse('home_app:home'))
        else:
            context['errors'].append('اطلاعات وارد شده صحیح نمی باشد')
            return render(self.request, self.template_name , context)
        return super(LoginFormView , self).form_valid(form)
class SignupFormView(LoginRequirdMixins , CreateView ):
    form_class = SignupForm
    template_name = 'account/register.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی اکانت'
        message = render_to_string('account/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return render(self.request, 'account/send_link.html')
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        Notification.objects.create(user=user , body = 'به سایت ما خوش امدید')
        return render(request, 'account/send_email_link2.html')
    else:
        return HttpResponse('Activation link is invalid!')
        
def logout_user(request):
    if request.user.is_authenticated == True:
        logout(request)
        return redirect(reverse('home_app:home'))
    else:
        return redirect(reverse('home_app:home'))

class UserProfile(LogoutRequirdMixins , TemplateView):
    template_name = 'account/user-panel.html'


def profile_edite(request):
    if request.user.is_authenticated == True:
        user = request.user
        form = Edite_Profile_Form(instance=user)
        if request.method == 'POST':
            form = Edite_Profile_Form(request.POST  , request.FILES ,instance=user)
            if form.is_valid():
                form.save()
                return redirect('account:profile')
        else:
            form = Edite_Profile_Form(instance=user)
        return render(request , 'account/edit-user-panel.html' , {'form':form})
    else:
        return redirect('home_app:home')