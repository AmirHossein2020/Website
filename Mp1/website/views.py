from django.shortcuts import render
from website.models import *
from website.forms import ContactForm
# Create your views here.

def home(request):
   cold_drink = Drinks.objects.filter(category = 1)
   hot_drink = Drinks.objects.filter(category = 2)
   juice_drink = Drinks.objects.filter(category = 3)
   context = {'hot_drink':hot_drink
              , 'cold_drink':cold_drink
              , 'juice_drink':juice_drink
              }
   return render(request, 'home.html', context)
def hot(request):
    hot_drink = Drinks.objects.filter(category = 2)
    context = {'hot_drink':hot_drink}
    return render(request, 'drink/hot.html', context)

def juice_drink(request):
    juice_drink = Drinks.objects.filter(category = 3)
    context = {'juice_drink':juice_drink}
    return render(request, 'drink/juice.html', context)

def about(request):
    about = Cafe.objects.all()
    context = {'abouttext':about}
    return render(request, 'about.html', context)
def special(request):
    special = Special_itmes.objects.all()
    context = {'special':special}
    return render(request, 'special.html', context)

def contact(request):
   special = Special_itmes.objects.all()
   if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
   form = ContactForm()
   context = {'form':form
              , 'special':special}
   return render(request, 'contact.html', context)