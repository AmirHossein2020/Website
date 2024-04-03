from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class  CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank = True)
    linkedin_link = models.CharField(max_length=255, null= True )
    github_link = models.CharField(max_length=255, null= True )
    phone = models.CharField(max_length=20, null= True )
    photo = models.ImageField(upload_to='profile/%Y/%m/%d/',default='null')

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=200)
    