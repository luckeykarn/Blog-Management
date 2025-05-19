from adminpanel.models import Category
from rest_framework import  viewsets
from .serializer import CategorySerializer

# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

