from django.shortcuts import render
from web.models import *

# Create your views here.

def home(request):
    ProductAll = Products.objects.all()
    context = {
        'proall':ProductAll,
    }
    return render(request, 'index.html' , context)


def about(request):
    return render(request, 'about.html')

def client(request):
    return render(request, 'client.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    PAll = Products.objects.all()
    context = {
        'proall':PAll,
    }
    return render(request, 'products.html',context)

def product(request, pk):
    product = Products.objects.get(id=pk)
    return render(request, 'singl.html', {'product': product})





