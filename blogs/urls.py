from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.my_blogs,name="my-blogs"), 
    path('create-blog/', views.create_blog,name="postblog"),
    path('blog/<slug:slug>', views.blog_detail,name="blog_detail"), # Using slug here original
    path('dashboard_blog/', views.dashboard,name="dashboard"), 
#     path('blog/<slug:slug>/', views.post_detail, name='post_detail'), # Using slug here
]
