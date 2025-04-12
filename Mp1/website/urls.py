from django.urls import path 
from website.views import *
from website import views

urlpatterns = [
    path('', views.home, name='home'),
]

""" path('drink/', views.Drink, name='drink'), """
""" path('about/', views.about, name='about'), """
""" path('special/', views.Special_items, name='special'), """
"""  path('contact/', views.Contact, name='contact'), """