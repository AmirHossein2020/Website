from django.shortcuts import render

# Create your views here.

def home(reqset):
    return render(reqset,'index.html')
