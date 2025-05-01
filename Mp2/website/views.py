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

def single_product(request, pk):
    singl_p = Product.objects.filter(id=pk)
    context = {'singl': singl_p}
    return render(request, 'singl.html', context)
def electronic(request):
    return render(request, 'electronic.html')

def fashion(request):
    return render(request, 'fashion.html')

def jewellery(request):
    return render(request, 'jewellery.html')