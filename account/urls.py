from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register,name="signup"),
    path('login/', views.user_login,name="user_login"),
    path('logout/', views.user_logout, name='userlogout'),
#     path('profile/', views.profile, name='profile'),
    path('profile-update/', views.Profile_Update,name="profile_update"),
    path('pernisson-error/', views.permission_error,name="permission_error"),
    path('author-profile/<str:username>/', views.author_profile, name='author_profile'),
   
    # password reset urls
    
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='reset_password/forgot_password.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='reset_password/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/password_reset_complete.html'),
         name='password_reset_complete'),
]
