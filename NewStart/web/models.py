from django.db import models
from datetime import date

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=100, null=True)
    bestphoto = models.ImageField(upload_to='media/photocity/%Y/%m/%d', null=True)

    def __str__(self):
        return self.name
    
class Restaurants(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    city = models.ForeignKey(to=City , on_delete = models.CASCADE)
    restaurantphoto = models.ImageField(upload_to='media/photorestaurants/%Y/%m/%d', null=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    city = models.ForeignKey(to=City , on_delete = models.CASCADE)
    htelphoto = models.ImageField(upload_to='media/photohotel/%Y/%m/%d', null=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
class Spectacular_location(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    city = models.ForeignKey(to=City , on_delete = models.CASCADE)
    photo = models.ImageField(upload_to='media/photolocation/%Y/%m/%d', null=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    title = models.CharField(max_length=50)
    comment = models.TextField(max_length = 200)
    photo = models.ImageField(upload_to='media/Comment/%Y/%m/%d', null=True)
    about = models.ManyToManyField(City)
    date = models.DateField(default=date.today)
    #author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
