from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns =[
    path('' , views.HomeView.as_view() , name='home'),
    # path('send_push', views.send_push , name='send_push'),
]