from comment.models import Comment
from rest_framework import  viewsets
from .serializer import CommentSerializer

# ViewSets define the view behavior.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
