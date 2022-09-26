from django.shortcuts import render
from blog.models import Categories


def Qeries(request):
    category = Categories.objects.all()
    return{'category':category}


