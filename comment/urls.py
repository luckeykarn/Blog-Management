from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('create-comment/<slug:blog_slug>/', views.create_comment,name="create_comment"), 
    path('view-comment/', views.comment_view,name="view_comment"), 

]