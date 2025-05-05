from django.db import models
# from django.contrib.auth.models import User
from account.models import CustomUser
from taggit.managers import TaggableManager  # pip install django-taggit
from django.utils.text import slugify
# from tinymce.widgets import TinyMCE



# Create your models here.
class Blogs(models.Model):
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) 
    content = models.TextField(blank=True,null=True)
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    # content = models.TextField()  # Just a TextField here
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Automatically set on update

    def __str__(self):
        return self.title

class BlogLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name="blog_like")
    blog  = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name="blog_like")

    class Meta:
        unique_together = ('user', 'blog')
