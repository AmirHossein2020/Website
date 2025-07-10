from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    address = models.TextField(null=True, blank=True)
    phon = models.IntegerField(null=True, blank=True)
    post_code = models.IntegerField(null=True, blank=True)