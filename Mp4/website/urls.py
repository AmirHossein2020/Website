from django import urls
from django.urls import path
from website.views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products_page,name='products-page'),
    path('search/', search_results, name='search_results'),
    path('products/sale/', products_page_sale,name='products-page-sale'),
    path('single/<int:pk>/', single_product, name='products'),
    path('ajax/add-to-cart/', ajax_add_to_cart, name='ajax_add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('ajax/remove-from-cart/', ajax_remove_from_cart, name='ajax_remove_from_cart'),

]