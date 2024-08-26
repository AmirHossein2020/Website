from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class  CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank = True)
    about = models.TextField(max_length=225,default='null')
    photo = models.ImageField(upload_to='profile/%Y/%m/%d/',default='null')
