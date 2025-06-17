from django.urls import path 
from web.views import *

urlpatterns = [
    path('', home, name='home'),
    path('cart', cart, name='cart'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),
    path('client/', client, name='client'),
    path('contact/', contact, name='contact'),
]
