from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index2.html')

def electronic(request):
    return render(request, 'electronic.html')

def fashion(request):
    return render(request, 'fashion.html')

def jewellery(request):
    return render(request, 'jewellery.html')