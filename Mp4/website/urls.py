from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', single_product, name='products'),

]