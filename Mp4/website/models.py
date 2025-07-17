from django.db import models

# Create your models here.
class Mall(models.Model):
    nameMall = models.CharField(max_length=400)
    address = models.TextField()
    call = models.IntegerField()
    email = models.EmailField()
    Linkinstegram = models.CharField(max_length=2000)
    Linkfacebook = models.CharField(max_length=2000)
    Linktwitter = models.CharField(max_length=2000)
    LinklinkedIn = models.CharField(max_length=2000)

    def __str__(self):
        return self.nameMall
    
class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    colour = models.CharField(max_length=250, null=True)
    style = models.CharField(max_length=250, null=True)
    price = models.IntegerField()
    about = models.TextField()
    image = models.ImageField(upload_to='product/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default = 0, decimal_places = 0, max_digits=12)

    def __str__(self):
        return self.name