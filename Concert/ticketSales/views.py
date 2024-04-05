from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from ticketSales.models import *
import accounts.views
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ticketSales.forms import *
import ticketSales.views
# Create your views here.

def concertListViews(request):

    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
         SearchText = searchForm.cleaned_data['SearchText']
         concerts = concertModel.objects.filter(Name__contains=SearchText)
    else:
        concerts = concertModel.objects.all()
    
    context = {

        "concertlist":concerts,
        "concertcount": concerts.count(),
        "searchForm": searchForm,

    }


    return render(request, "ticketSales/concertlist.html",context)

@login_required
def locationListViews(request):
    locations = locationModel.objects.all()
    
    context = {

        "locationlist": locations,
    }


    return render(request, "ticketSales/locationlist.html",context)

def concertDetailsViews(request, concert_id):
    concert = concertModel.objects.get(pk=concert_id)

    context = {
        "concertdetails":concert
    }

    return render(request, "ticketSales/cocertDetails.html",context)

@login_required
def timeViews(request):
    #if request.user.is_authenticated and request.user.is_active:

        times = timeModel.objects.all()

        context = {

            "timelist": times,
        }

        return render(request, "ticketSales/timeList.html",context)
    #else:
       # return HttpResponseRedirect(reverse(accounts.views.loginView))

def concertEditView(request,concert_id):
     concert = concertModel.objects.get(pk=concert_id)
     if request.method == "POST":
          concertForm = ConcertForm(request.POST,request.FILES ,instance=concert)
          if concertForm.is_valid():
               concertForm.save()
               return HttpResponseRedirect(reverse(ticketSales.views.concertListViews))
     else:
        concertForm = ConcertForm(instance=concert)

     context = {
          "concertForm" : concertForm,
          "PosterImage":concert.Poster,
     }

     return render(request, "ticketSales/concertEdit.html",context)