from blogs.models import Blogs,BlogLike
from rest_framework import  serializers

# Serializers define the API representation.
class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = "__all__"

class BlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLike
        fields = "__all__"