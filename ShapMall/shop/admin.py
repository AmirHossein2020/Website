# در این بخش ادمین ما مدل های که
# برای سایت در مدل ها ساختیم و یه جنگو معرفی میکنیم
# ...تا اونا را به ما نمایش بده با استفاده از دستورات زیر
from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)