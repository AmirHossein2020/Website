from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request, 'index.html')

def AbuotView(request):
    return render(request, 'about.html')