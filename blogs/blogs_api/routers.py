from django.urls import path, include
from blogs.models import Blogs,BlogLike
from rest_framework import routers
from .viewset import BlogsViewSet,BlogLikeViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'blogs', BlogsViewSet)
router.register(r'bloglike', BlogLikeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]