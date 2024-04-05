from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = "کاربر",related_name = "profile")

   
    ProfileImage = models.ImageField(upload_to="ProfileImages/")

    Man = 1
    Woman = 2
    status_chioces = ((Man,"مرد"),(Woman,"زن"))

    Gender = models.IntegerField(choices = status_chioces)

    Credit = models.IntegerField(verbose_name="اعتبار",default=0)

    