"""
URL configuration for mainapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
     # Web Endpoints

    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')), 
    path('adminpanel/', include('adminpanel.urls')), 
    path('', include('blogs.urls')), 
    path('comments/', include('comment.urls')), 

    # API Endpoints
    path('api/', include('blogs.blogs_api.routers')),  
    path('api/token/', obtain_auth_token, name='api_token_auth'),  # new token login
    path('api/', include('adminpanel.adminpanel_api.routers')),
    path('api/', include('account.account_api.routers')),
    path('api/', include('comment.comment_api.routers')), 

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)