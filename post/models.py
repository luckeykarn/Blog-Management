from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager  # pip install django-taggit
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True) 
    content = models.TextField(blank=True,null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Automatically set on update

    def __str__(self):
        return self.title