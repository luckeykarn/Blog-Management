from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    profile_picture = models.ImageField(upload_to="account")

    bio = models.TextField(blank=True)
   
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

