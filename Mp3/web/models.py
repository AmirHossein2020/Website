from django.db import models
from django.conf import settings
# Create your models here.

class Mall(models.Model):
    nameMall = models.CharField(max_length=400)
    customer = models.CharField(max_length=500)
    address = models.TextField()
    call = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to="mall/customer")
    aboutcustomer = models.TextField()
    BestProducts = models.TextField()
    Linkinstegram = models.CharField(max_length=2000)
    Linkfacebook = models.CharField(max_length=2000)
    Linktwitter = models.CharField(max_length=2000)
    LinklinkedIn = models.CharField(max_length=2000)

    def __str__(self):
        return self.nameMall
    

class Products(models.Model):
    name = models.CharField(max_length=500)
    about = models.TextField()
    price = models.IntegerField()
    priceoff = models.IntegerField()
    image = models.ImageField(upload_to="product/image")

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"

# آیتم داخل سبد خرید
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"