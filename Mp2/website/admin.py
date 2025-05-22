from django.contrib import admin
from website.models import *
# Register your models here.

admin.site.register(Mall)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category_Clothes)