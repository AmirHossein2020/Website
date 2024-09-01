from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estate(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    location = models.CharField(max_length=2000, null=True)
    phone = models.IntegerField()
    landline_phone = models.IntegerField()
    email = models.EmailField()
    about = models.TextField()

    def __str__(self):
        return self.name
    
class HouseCategory(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class HouseModel(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.url   
    

class HomeFile(models.Model):
    model = models.ForeignKey(HouseModel, on_delete=models.CASCADE)
    type = models.ForeignKey(HouseCategory, on_delete=models.CASCADE)
    meterage = models.IntegerField(null=True)
    rooms = models.IntegerField(null=True)
    bathroom = models.IntegerField(null=True)
    wc = models.IntegerField(null=True)
    mortage_price = models.IntegerField()
    rental_price = models.IntegerField()
    selling_price = models.IntegerField()
    address = models.CharField(max_length=500, default="")
    about = models.TextField()
    phonehome = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images/home/')
    image2 = models.ImageField(upload_to='images/home/2')
    image3 = models.ImageField(upload_to='images/home/3',null=True)
    image4 = models.ImageField(upload_to='images/home/4', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
    
class Massega(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=500)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name