from django.urls import path
from website.views import *
urlpatterns = [
   path('', home,name='home'),
   path('about', about_us, name='about'),
   path('Branches', branche, name='branche'),
   path('Branche/<int:pk>', Branche_singl.as_view(), name='B_singl'),
    
]

