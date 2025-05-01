from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>', single_product, name= 'singl'),
    path('electronic/', electronic, name='electronic'),
    path('fashion/', fashion, name='fashion'),
    path('jewellery/', jewellery, name='jewellery'),
]