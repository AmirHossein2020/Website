from django.shortcuts import render , redirect
from web.models import HouseCategory , HouseModel , HomeFile
from web.forms import PostFile
from django.urls import reverse_lazy 
from django.views.generic import  View ,FormView, CreateView ,ListView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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

class FileNewView(CreateView):
    model = HomeFile
    template_name = 'home_new.html'
    form_class = PostFile
    success_url = reverse_lazy('home')

def vew(request):
    user = request.user
    form = PostFile(initial={'author': user})
    return render(request, 'home_new.html', {'form': form,'user': user})

def my_view(request):
    if request.method == 'POST':
        form = PostFile(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to the home page
    else:
        form = PostFile(user=request.user)
    return render(request, 'home_new.html', {'form': form})

