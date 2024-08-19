from django.db import models
from django.utils import timezone

# Create your models here.

class Language(models.Model):
    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.languages
    
class Language_persian(models.Model):
    languages_persian = models.CharField(max_length=100)

    def __str__(self):
        return self.languages_persian

class Professional_skill(models.Model):
    professional_skill = models.CharField(max_length=100)

    def __str__(self):
        return self.professional_skill
    
class Professional_skill_persian(models.Model):
    professional_skill_persian = models.CharField(max_length=100)

    def __str__(self):
        return self.professional_skill_persian

class Resume(models.Model):
    experiencename = models.CharField(max_length=20)
    aboutexperience = models.TextField(max_length=200)
    experiencename_persian = models.CharField(max_length=20, default='null')
    aboutexperience_persian = models.TextField(max_length=200, default='null')
    startyear = models.DateField(default=timezone.now)
    endyear = models.DateField(default=timezone.now)
    nameinstitute = models.CharField(max_length=20)
    nameinstitute_persian = models.CharField(max_length=200, default='null')
    startyear_education = models.DateField(default=timezone.now)
    endyear_education = models.DateField(default=timezone.now)
    namecity = models.CharField(max_length=200, default='null')
    abuotinstitute = models.TextField(max_length=100)
    namecity_persian = models.CharField(max_length=200, default='null')
    abuotinstitute_persian = models.TextField(max_length=250, default='null')
    professional_skill = models.ManyToManyField(Professional_skill, related_name="skill")
    professional_skill_persian = models.ManyToManyField(Professional_skill_persian, related_name="s_persian")
    language = models.ManyToManyField(Language, related_name="language")
    language_persian = models.ManyToManyField(Language_persian, related_name="l_persian")

    def __str__(self):
        return self.experiencename
    
class Project(models.Model):
    nameproject = models.CharField(max_length=50)
    abuotproject = models.TextField(max_length = 200)
    nameproject_persian = models.CharField(max_length=250, null = True)
    abuotproject_persian = models.TextField(max_length = 500, null = True)
    photoproject = models.ImageField(upload_to='project/%Y/%m/%d')

    def __str__(self):
         return self.nameproject
     
class Abuot(models.Model):
    title = models.CharField(max_length=250)
    title_persian = models.CharField(max_length=250)
    body = models.TextField()
    body_persian = models.TextField()
    linkedin_link = models.CharField(max_length=255, null= True )
    github_link = models.CharField(max_length=255, null= True )
    phone = models.CharField(max_length=20, null= True )
    email = models.EmailField(null= True)


    def __str__(self):
        return self.title
    

