from django.urls import path 
from web.views import *

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('products/', products, name='products'),
    path('product/<int:pk>/', product, name="product"),
    path('about/', about, name='about'),
    path('client/', Mallitem, name='Mall'),
]
