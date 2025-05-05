from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator , MinValueValidator
import datetime
# Create your models here.

class UserSite(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    email = models.EmailField()
    phon = models.IntegerField()
    post_code = models.IntegerField()

    def __str__(self):
       return self.name

class Mall(models.Model):
    name = models.CharField(max_length=250)
    about = models.TextField()
    addess = models.TextField()

    def __str__(self):
       return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    about = models.TextField()
    image = models.ImageField(upload_to='product/')
    category = models.ManyToManyField(Category)
    star = models.IntegerField(default =0, validators = [MaxValueValidator(5), MinValueValidator(0)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default = 0, decimal_places = 0, max_digits=12)

    def __str__(self):
        return self.name

# مدل سبد خرید
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"

# آیتم داخل سبد خرید
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

