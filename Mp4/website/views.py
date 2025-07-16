from django.shortcuts import render

# Create your views here.

def home(reqset):
    return render(reqset,'index.html')

def cart(reqset):
    return render(reqset,'cart.html')

def single_product(reqset):
    return render(reqset,'single-product.html')