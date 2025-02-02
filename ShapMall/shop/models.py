# در بخش مدل ها باید بخش های مختلف 
# سایت و در اینجا بسازیم یعنی تعیین کنیم که چه قابلیت های میخواهیم و اونارو تو
# این بخش انجامبدیم نکته مهم
# این هست بعد هر تغییری تو این بخش باید تغیرات و منتقل کنیم به دیتابیس

from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20,  blank = True)
    picture = models.ImageField(upload_to='upload/category/',  blank = True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone  = models.CharField(max_length=20)
    emali = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    price = models.DecimalField(default = 0, decimal_places = 0, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='upload/product/')
    star = models.IntegerField(default =0, validators = [MaxValueValidator(5), MinValueValidator(0)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default = 0, decimal_places = 0, max_digits=12)


    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default =1)
    address = models.CharField(max_length = 400, default = '', blank = True)
    phone = models.CharField(max_length =20, blank = True)
    date = models.DateField(default = datetime.datetime.today())
    status = models.IntegerField(default =False)

    def __str__(self):
        return self.product