from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),

]