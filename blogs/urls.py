from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.my_blogs,name="my-blogs"), 
    path('blog/', views.blog_detail,name="blog_detail"), 
    path('create-blog/', views.create_blog,name="postblog"), 
]
