from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request, 'website/index.html')

def AbuotView(request):
    return render(request, 'website/about.html')

def ContactView(request):
    return render(request, 'website/contact.html')