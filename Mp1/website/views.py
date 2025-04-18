from django.shortcuts import render
from website.models import *
# Create your views here.

def home(request):
   about = Cafe.objects.all()
   context = {'abouttext':about}
   return render(request, 'home.html', context)







""" def Contact(request):
   return render(request, 'contact.html')
 """

