from django.db import models
from .models import Post

# Create your models here.
post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
name = models.CharField(max_length=100)
email = models.EmailField()
body = models.TextField()
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f'Comment by {self.name} on {self.post.title}'