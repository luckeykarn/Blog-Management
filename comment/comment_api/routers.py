from django.urls import path, include
from comment.models import Comment
from rest_framework import routers
from .viewset import CommentViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)

# Wire up our API using automatic URL routing.

urlpatterns = [
    path('', include(router.urls)),
]