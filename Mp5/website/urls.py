from django.urls import path
from website.views import *
urlpatterns = [
   path('', home,name='home'),
    
]

