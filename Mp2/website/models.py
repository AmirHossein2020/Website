from django.db import models
import datetime
# Create your models here.

class UserSite(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    email = models.EmailField()
    phon = models.IntegerField()
    post_code = models.IntegerField()

    def __str__(self):
        self.name

class Mall(models.Model):
    name = models.CharField(max_length=250)
    about = models.TextField()
    addess = models.TextField()

    def __str__(self):
        self.name

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    about = models.TextField()
    image = models.ImageField(upload_to='product/')
    discount = models.IntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        self.name

