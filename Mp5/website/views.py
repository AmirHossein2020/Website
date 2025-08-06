from django.shortcuts import render
from website.models import *
from django.views.generic import DetailView 
from website.forms import *
# Create your views here.


def home(request):
    price_off = Pricing_off.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    context = {
        'form': form,
        'off': price_off
    }
    return render(request, 'index.html', context)


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
    context_object_name = 'branch' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch = self.get_object()
        deserts = Meno_desert.objects.filter(branche=branch)
        dishs = Meno_dish.objects.filter(branche=branch)
        starters = Meno_starter.objects.filter(branche=branch)
        dreinks = Meno_dreink.objects.filter(branche=branch)
        context['deserts'] = deserts
        context['dishs'] = dishs
        context['starters'] = starters
        context['dreinks'] = dreinks
        return context