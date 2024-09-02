from django.shortcuts import render , redirect
from web.models import HouseCategory , HouseModel , HomeFile, Massega , Estate
from web.forms import PostFile , SearchForm , FormComment
from django.urls import reverse_lazy 
from django.views.generic import  View ,FormView, CreateView ,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.

def HomePage(request):
    category = HouseModel.objects.all()
    context = {'category':category}
    return render(request, 'index.html',context)

def estate_admin(request):
    """
    Return a list of all the estate in the estate table
    """
    estates = Estate.objects.all()
    context = {'estates': estates}
    return render(request, 'about.html', context)


def category(request, cat):
    category = HouseModel.objects.get(name= cat)
    file = HomeFile.objects.filter(model = category)
   
    context = {
        'file': file,
        'category': category,
    }
    return render(request, 'listhome.html',context)

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


def my_view(request):
    if request.method == 'POST':
        form = PostFile(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to the home page
    else:
        form = PostFile(user=request.user)
    return render(request, 'home_new.html', {'form': form})


class form_comment(CreateView):
    model = Massega
    form_class = FormComment
    template_name = 'about.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estates'] = Estate.objects.all()
        return context

def fileListViews(request):

    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        SearchText = searchForm.cleaned_data['SearchText']
        file = HomeFile.objects.filter(mortage_price__contains=SearchText)
    else:
        file = HomeFile.objects.all()
    
    context = {

        "file":file,
        "searchForm": searchForm,

    }

    return render(request, "listall.html",context)

class UpdateView(UpdateView):
    model = HomeFile
    template_name = 'home_update.html'
    fields = ['model', 'type', 'meterage', 'rooms',
                'bathroom', 'wc', 'mortage_price', 'rental_price',
                'selling_price', 'address', 'about', 'phonehome', 'image',
                'image2', 'image3', 'image4']
    success_url = reverse_lazy('home')