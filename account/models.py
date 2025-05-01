from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(choices=(('admin','Admin'),('author','Author'),('user','User')))
    image = models.ImageField(upload_to="account")
    gender =  models.CharField(choices=(('male','Male'),('female','Female'),('others','Others')))
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['username']

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # is_author = models.BooleanField(default=False)
#     # is_user = models.BooleanField(default=True)

#     role = models.CharField(choices=(('admin','Admin'),('author','Author'),('user','User')))


#     def __str__(self):
#         return self.user.username