from django.urls import path , re_path , include
from . import views


app_name = 'account'


urlpatterns = [
    path('login/' , views.LoginFormView.as_view(), name='login'),
    path('logout/' , views.logout_user , name='logout'),
    path('register/' , views.SignupFormView.as_view() , name='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
    views.activate, name='activate'),  
    path('profile' , views.UserProfile.as_view() , name='profile'),
    path('profile-edit' , views.profile_edite , name='profile-edit'),
    # path('/password_change' , views.change_passwords , name='password_change'),
    # path('/password_change' , views.change_passwords , name='password_change'),
]
