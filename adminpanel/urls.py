from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.author_dashboard, name='author_dashboard'),
    path('author-blog/', views.author_blog, name='author_blog'),
    path('profile-setting/', views.profile_settings, name='profile_settings'),
    path('add-post/', views.add_post, name='add_post'),
    path('edit-post/<int:id>', views.post_edit, name='post_edit'),
    path('categories/', views.categories, name='categories'),
    path('update-category/', views.update_category, name='update_category'),
    path('delete-category/', views.delete_category, name='delete_category'),
    path('nav-bar/', views.navbar, name='navbar'),
    path('profile-view/', views.profile_view, name='profile_view'),
 
 
    
]



