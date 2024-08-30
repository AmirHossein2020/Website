from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estate(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.IntegerField(max_length=11)
    landline_phone = models.IntegerField(max_length=8)
    email = models.EmailField()
    about = models.TextField()

    def __str__(self):
        return self.name
    
class HouseCategory(models.Model):
    type = models.CharField(max_length=500)

    def __str__(self):
        return self.type

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
    meterage = models.IntegerField(max_length=1000)
    rooms = models.IntegerField(max_length=10)
    bathroom = models.IntegerField(max_length=10)
    wc = models.IntegerField(max_length=10)
    mortage_price = models.IntegerField()
    rental_price = models.IntegerField()
    selling_price = models.IntegerField()
    address = models.CharField(max_length=500)
    about = models.TextField()
    phonehome = models.IntegerField(max_length=11)
    image = models.ImageField(upload_to='images/home/')
    images = models.ManyToManyField(Image)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address