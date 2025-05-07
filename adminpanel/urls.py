from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.author_dashboard, name='author_dashboard'),
    path('categories/', views.categories, name='categories'),
    path('author-blog/', views.author_blog, name='author_blog'),
    path('setting/', views.setting, name='setting'),

]



