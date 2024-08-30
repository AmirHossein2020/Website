from django.shortcuts import render
from web.models import HouseCategory , HouseModel , HomeFile

# Create your views here.

def HomePage(request):
    return render(request, 'index.html')

def category(request, cat):
    category = HouseModel.objects.get(name= cat)
    file = HomeFile.objects.filter(model = category)
    return render(request, 'listhome.html', {'file': file, 'category': category})

def category_type(request, pid):
    category_type = HouseCategory.objects.filter(type= pid)
    file = HomeFile.objects.filter(type = category_type)
    return render(request, 'listhome.html', {'file_type': file, 'category_type': category_type})