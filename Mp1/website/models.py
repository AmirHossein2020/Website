from django.db import models

# Create your models here.

class Cafe(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    about = models.TextField()
    location = models.TextField(null=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Drinks(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField(max_length=10)
    Description = models.TextField()
    imge = models.ImageField(upload_to='images/')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
   

class Special_itmes(models.Model): 
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.IntegerField(max_length=10)
    imge = models.ImageField(upload_to='images/special/',null=True)

    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
   
