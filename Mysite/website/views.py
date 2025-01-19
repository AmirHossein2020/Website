from django.shortcuts import render
from website.forms import ContactForm , Newsletterform
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.

def HomeView(request):
    return render(request, 'website/index.html')

def AbuotView(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        forms = Newsletterform(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')