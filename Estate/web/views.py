from django.shortcuts import render
from web.models import HouseCategory , HouseModel , HomeFile

# Create your views here.

def HomePage(request):
    category = HouseModel.objects.all()
    context = {'category':category}
    return render(request, 'index.html',context)

def category(request, cat):
    category = HouseModel.objects.get(name= cat)
    file = HomeFile.objects.filter(model = category)
    return render(request, 'listhome.html', {'file': file, 'category': category})

def home_type(request, pid):    
    category = HouseCategory.objects.get(name= pid)
    file = HomeFile.objects.filter(type = category)
    context =  {'file': file,
                'category': category,
                }
    return render(request, 'type.html',context)

def SingleHome(request,pid):
    home = HomeFile.objects.filter(pk=pid)
    context = {'home': home}
    return render(request, 'Homefile.html', context)