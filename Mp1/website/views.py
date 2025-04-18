from django.shortcuts import render
from website.models import *
# Create your views here.

def home(request):
   about = Cafe.objects.all()
   hot_drink = Drinks.objects.filter(category = 2)
   cold_drink = Drinks.objects.filter(category = 1)
   juice_drink = Drinks.objects.filter(category = 3)
   context = {'abouttext':about
              , 'hot_drink':hot_drink
              , 'cold_drink':cold_drink
              , 'juice_drink':juice_drink}
   return render(request, 'home.html', context)







""" def Contact(request):
   return render(request, 'contact.html')
 """

