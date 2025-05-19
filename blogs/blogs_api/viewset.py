from blogs.models import Blogs,BlogLike
from rest_framework import  viewsets
from .serializer import BlogsSerializer,BlogLikeSerializer

# ViewSets define the view behavior.
class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

class BlogLikeViewSet(viewsets.ModelViewSet):
    queryset = BlogLike.objects.all()
    serializer_class = BlogLikeSerializer