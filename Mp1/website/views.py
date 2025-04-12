from django.shortcuts import render
from website.models import *
# Create your views here.

def home(request):
   return render(request, 'home.html')


""" def Drink(request):
   return render(request, 'drink.html')
"""


""" def about(request):
   return render(request, 'about.html') """


""" def Special_items(request):
   return render(request, 'special.html')
"""


""" def Contact(request):
   return render(request, 'contact.html')
 """

