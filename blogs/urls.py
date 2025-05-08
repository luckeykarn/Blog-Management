from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.my_blogs,name="my-blogs"), 
    path('create-blog/', views.create_blog,name="postblog"),
    path('blog/<slug:slug>', views.blog_detail,name="blog_detail"), # Using slug here original 
    path('like-blog/', views.like_blog,name="like_blog"), 
    path('search_post/', views.search, name='search'), 
    path('tag/<slug:tag_slug>/', views.blogs_by_tag, name='blogs_by_tag'), # for tag filtering
    
]


