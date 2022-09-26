from django import forms
from .models import User
from django.contrib.auth import authenticate, login
from django.core.validators import ValidationError
from matplotlib import widgets
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField( max_length=50  , widget = forms.TextInput(attrs={'class': 'email-input','placeholder':' پست الکترونیک یا شماره تلفن'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-input' , 'placeholder':'گذرواژه'}) )


    # def clean_email(email):
    #     all_email = User.objects.all()
    #     for email in all_email:
    #         if email != email.email :
    #             raise ValidationError('informations is not correct')
    #         else:
    #             raise ValidationError('amir')
    # def clean_password(self):
    #     user = authenticate(email = self.cleaned_data.get('email') , password = self.cleaned_data.get('password'))
    #     if user is not None:
    #         return self.cleaned_data.get('password')
    #     else:
    #          raise ValidationError('informations is not correct' , code='invalid-errors')

class SignupForm(UserCreationForm):
    email = forms.CharField(widget = forms.EmailInput(attrs={'class': 'email-input' , 'placeholder':'پست الکترونیک'}) , required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-input' , 'placeholder':'گذرواژه'}) , required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-input' , 'placeholder':'تکرار گذرواژه'}) , required=True)
    class Meta:
        model = User
        fields = ('email', 'password1' , 'password2')
        widgets={
            'email':forms.EmailInput(attrs={'class':'email-input' , 'placeholder':'پست الکترونیک'})
        }

class Edite_Profile_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=['Full_name', 'username' , 'email' , 'number' , 'image']
        widgets={
            'username':forms.TextInput(attrs={'class':'email-input' , 'placeholder':'نام کاربری'}),
            'Full_name' :forms.TextInput(attrs={'class':'email-input' , 'placeholder':'نام و نام خانوادگی'}),
            'number' :forms.TextInput(attrs={'class':'email-input' , 'placeholder':'شماره تلفن'}),
            'email' :forms.TextInput(attrs={'class':'email-input' , 'placeholder':'پست الکترونیک'}),
        }
