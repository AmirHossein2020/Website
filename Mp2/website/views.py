from django.shortcuts import render
from website.models import *
# Create your views here.

def home(request):
    labtops = Product.objects.filter(category = 1)
    Tshirts = Product.objects.filter(category = 2)
    jewellerys = Product.objects.filter(category = 3)
    context = {'labtops':labtops,
               'Tshirts':Tshirts,
               'jewellerys':jewellerys}
    return render(request, 'home.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'singl.html', {'product': product})

def electronic(request):
    return render(request, 'electronic.html')

def fashion(request):
    return render(request, 'fashion.html')

def jewellery(request):
    return render(request, 'jewellery.html')