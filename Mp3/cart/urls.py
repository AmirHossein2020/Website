from django.urls import path 
from cart.views import *

urlpatterns = [
    path('ajax/add-to-cart/', ajax_add_to_cart, name='ajax_add_to_cart'),
    path('', cart_detail, name='cart_detail'),
    path('ajax/remove-from-cart/', ajax_remove_from_cart, name='ajax_remove_from_cart'),
]