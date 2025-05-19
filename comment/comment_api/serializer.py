from comment.models import Comment
from rest_framework import  serializers

# Serializers define the API representation.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"