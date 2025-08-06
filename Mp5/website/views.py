from django.shortcuts import render
from website.models import *
# Create your views here.


def home(request):

    return render(request, 'index.html')

def about_us(request):
    abus = about.objects.all()
    context = {
        'abus':abus,
    }
    return render(request,'about.html',context)

def branche(request):
    brancheR = Branches.objects.all()
    context = {
        'brancheR':brancheR,
    }
    return render(request, 'branches.html', context)

def menoB(request,pk):
    menoDe = Meno_desert.objects.filter(pk=Branches)
    context = {
        'desert':menoDe,
    }
    return render(request, 'meno.html', context)