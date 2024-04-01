from django.db import models
from django.utils import timezone

# Create your models here.


class Resume(models.Model):
    experiencename = models.CharField(max_length=20)
    aboutexperience = models.TextField(max_length=200)
    startyear = models.DateField(default=timezone.now)
    endyear = models.DateField(default=timezone.now)
    nameinstitute = models.CharField(max_length=20)
    startyear_education = models.DateField(default=timezone.now)
    endyear_education = models.DateField(default=timezone.now)
    namecity = models.CharField(max_length=20, default='null')
    abuotinstitute = models.TextField(max_length=100)
    professional_skill = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.experiencename
    
class Project(models.Model):
     nameproject = models.CharField(max_length=50)
     abuotproject = models.TextField(max_length = 200)
     photoproject = models.ImageField(upload_to='project/%Y/%m/%d')

     def __str__(self):
         return self.nameproject