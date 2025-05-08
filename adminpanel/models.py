from django.db import models
from account.models import CustomUser
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # slug = models.SlugField(max_length=100, unique=True)
   
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

# models.py
from django.contrib.auth.models import User
from django.db import models

