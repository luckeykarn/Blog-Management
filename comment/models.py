from django.db import models
from blogs.models import Blogs
from account.models import CustomUser

# Create your models here.
class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='user_comments')
    # name = models.CharField(max_length=100) #hide because user relation already present, in user model there is already name and email
    # email = models.EmailField()
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return f"Comment by {self.user.username}"
    