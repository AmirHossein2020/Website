from django.shortcuts import render
from web.models import *
from accounts.models import *
from web.forms import *

# Create your views here.

def home(request):
    mallitem = Mall.objects.all()
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
         SearchText = searchForm.cleaned_data['SearchText']
         ProductAll = Products.objects.filter(name__contains=SearchText)
    else:
        ProductAll = Products.objects.all()
    context = {
        'proall':ProductAll,
        'item': mallitem,
        "searchForm": searchForm,
        
    }
    return render(request, 'index.html' , context)

def profile(request):
    if request.user.is_authenticated:
        profile_user = CustomUser.objects.get(id=request.user.id)
        context = {
            'profile': profile_user
        }
        return render(request, 'registration/Profile.html', context)
    else:
        return render(request, 'registration/Profile.html', {'profile': None, 'message': 'Please log in to view your profile.'})


def about(request):
    abouttext = Mall.objects.all()
    context = {
        'item': abouttext
    }
    return render(request, 'about.html', context)

def Mallitem(request):
    itmes = Mall.objects.all()
    context = {
        'item': itmes,
        
    }
    return render(request, 'base.html', context)



def products(request):
    PAll = Products.objects.all()
    context = {
        'proall':PAll,
    }
    return render(request, 'Products/products.html',context)

def product(request, pk):
    product = Products.objects.get(id=pk)
    return render(request, 'Products/singl.html', {'product': product})


