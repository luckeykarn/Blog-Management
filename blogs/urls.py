from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.my_blogs,name="my-blogs"), 
    path('create-blog/', views.create_blog,name="postblog"), 
]
