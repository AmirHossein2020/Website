from django.urls import path 
from web.views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('product/<int:pk>/', product, name="product"),
    path('about/', about, name='about'),
    path('client/', client, name='client'),
    path('contact/', contact, name='contact'),
]
