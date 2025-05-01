from django.db import models
from blogs.models import Blogs

# Create your models here.
class Comment(models.Model):
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return f'Comment by {self.name}'
    