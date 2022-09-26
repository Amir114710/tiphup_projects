from django.urls import reverse
from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import TemplateView , DetailView , View , ListView
from .models import Comments, Like, Post , Categories , Notification
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.core.paginator import Paginator
class BlogView(ListView):
    model = Post
    template_name = 'blog/all-videos.html'
    paginate_by = 6
    context_object_name = 'posts'
    def get_context_data(self , *args, **kwargs):
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        if self.request.user.notifications.filter(user_id=self.request.user.id):
            context['notifications'] = Notification.objects.all()
        else:
            pass
        return context

class DetailsViewPost(DetailView):
    model = Post
    template_name = 'blog/video-detail.html'
    context_object_name = 'posts'
    queryset = None
    def get_context_data(self , *args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)
        queryset = Post.objects.get(slug = self.object.slug)
        queryset.views += 1
        queryset.save()
        if self.request.user.likes2.filter(posts__title = self.object.title , users_id = self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context 
    def post(self,request,slug):
        posts = Post.objects.get(slug=slug)
        parent_id = request.POST.get('parent_id')
        message = request.POST.get('message')
        Comments.objects.create(message=message, parent_id=parent_id , posts=posts , user=request.user)
        if Comments.parent is not None:
            Notification.objects.create(user=request.user , body='نظر شما با موفقیت ثبت شد')
        return redirect('blog_app:details' , slug)
    # def get(self,request,slug):
    #     queryset = Post.objects.get(slug = slug)
    #     queryset.views += 1
    #     queryset.save()
    #     return render(request, self.template_name , {'posts':queryset})
class Category_details(View):
    queryset = None
    template_name = 'blog/all-videos.html'
    def get(self, request , pk):
        queryset = get_object_or_404(Categories , id=pk)
        objects = queryset.posts.all()
        return render (request , self.template_name , {'id':pk , 'posts':objects})

class SearchBox(TemplateView):
    queryset = None
    template_name = 'blog/all-videos.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        queryset = Post.objects.filter(title__icontains = q)
        page_number = request.GET.get('page')
        paginator = Paginator(queryset , 6)
        objects = paginator.get_page(page_number)
        return render(request, self.template_name, {'posts': objects})

def like(request , slug , pk):
    try:
        like = Like.objects.get(posts__slug = slug , users_id=request.user.id)
        like.delete()
        return JsonResponse({"response" : "unliked"})
    except:
        Like.objects.create(posts_id=pk , users_id = request.user.id)
        return JsonResponse({"response" : "liked"})

    # return redirect('blog_app:details' , slug)



