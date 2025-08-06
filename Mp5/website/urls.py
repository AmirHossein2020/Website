from django.urls import path
from website.views import *
urlpatterns = [
   path('', home,name='home'),
   path('about', about_us, name='about'),
   path('Branches', branche, name='branche')
    
]

