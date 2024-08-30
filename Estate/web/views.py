from django.shortcuts import render
from web.models import HouseCategory , HouseModel , HomeFile

# Create your views here.

def HomePage(request):
    return render(request, 'index.html')

def category(request, cat):
    category1 = HouseModel.objects.get(name= cat)
    file = HomeFile.objects.filter(model = category1)
    return render(request, 'listhome.html', {'file': file, 'category': category1})

