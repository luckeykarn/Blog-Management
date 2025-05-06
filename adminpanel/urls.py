from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.author_dashboard, name='author_dashboard'),
]


