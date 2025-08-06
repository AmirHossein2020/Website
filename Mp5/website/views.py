from django.shortcuts import render
from website.models import *
from django.views.generic import ListView , DetailView ,View, TemplateView , CreateView
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

class Branche_singl(DetailView):
    model = Branches
    template_name = 'meno.html'

def menoB(request,pk):
    B = Branches.objects.get(id=pk)
    menoDe = Meno_desert.objects.filter(B=B)
    context = {
        'branch':B,
        'deserts':menoDe,
    }
    return render(request, 'meno.html', context)