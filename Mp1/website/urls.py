from django.urls import path 
from website.views import *


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('special/', special, name='special'),
]

""" path('drink/', views.Drink, name='drink'), """
""" path('about/', views.about, name='about'), """
""" path('special/', views.Special_items, name='special'), """
"""  path('contact/', views.Contact, name='contact'), """