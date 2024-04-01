from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class  CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank = True)
    about = models.TextField(max_length=225,default='null')
    photo = models.ImageField(upload_to='profile/%Y/%m/%d/',default='null')

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=200)
    