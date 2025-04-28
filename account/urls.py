from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register,name="signup"),
    path('login/', views.user_login,name="user_login"),
    path('logout/', views.user_logout, name='userlogout'),
    # path('profile/', views.profile, name='profile'),
]