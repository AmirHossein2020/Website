from django.shortcuts import render
from website.models import *
from website.forms import ContactForm
# Create your views here.

def home(request):
   about = Cafe.objects.all()
   hot_drink = Drinks.objects.filter(category = 2)
   cold_drink = Drinks.objects.filter(category = 1)
   juice_drink = Drinks.objects.filter(category = 3)
   special = Special_itmes.objects.all()
   if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
   form = ContactForm()
   context = {'abouttext':about
              , 'hot_drink':hot_drink
              , 'cold_drink':cold_drink
              , 'juice_drink':juice_drink
              , 'special':special
              , 'form':form}
   return render(request, 'home.html', context)

