from django.shortcuts import render
from blog.models import Categories, Notification , Post


def Qeries(request):
    category = Categories.objects.all()
    posts = Post.objects.all()
    return{'category':category , 'posts':posts}



