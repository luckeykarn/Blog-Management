from django.urls import path, include
from account.models import CustomUser
from rest_framework import routers
from .viewset import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

# Wire up our API using automatic URL routing.

urlpatterns = [
    path('', include(router.urls)),
]