from django.urls import path, include
from adminpanel.models import Category
from rest_framework import routers
from .viewset import CategoryViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)

# Wire up our API using automatic URL routing.

urlpatterns = [
    path('', include(router.urls)),
]