from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('details/<slug:slug>' , views.DetailsViewPost.as_view() , name='details'),
    path('blog' , views.BlogView.as_view() , name='blog'),
    path('categories/<int:pk>' , views.Category_details.as_view() , name='category'),
    path('like/<slug:slug>/<int:pk>' , views.like , name='like'),
    path('search' , views.SearchBox.as_view() , name='search'),
]

