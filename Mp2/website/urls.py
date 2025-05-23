from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', product, name="product"),
    path('ajax/add-to-cart/', ajax_add_to_cart, name='ajax_add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('ajax/remove-from-cart/', ajax_remove_from_cart, name='ajax_remove_from_cart'),
    path('electronic/', electronic, name='electronic'),
    path('fashion/', fashion, name='fashion'),
    path('jewellery/', jewellery, name='jewellery'),
    path('category/<str:cat>/', category, name="category"),
    path('category_summary/', category_summary, name="category_summary"),
]