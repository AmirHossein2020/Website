from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from web.models import *
from django.views.generic import ListView , DetailView ,View, TemplateView , CreateView
from .forms import FormRestaurant , SearchForm , FormComment
from django.urls import reverse , reverse_lazy
# Create your views here.

def  HomeView(request):

    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
         SearchText = searchForm.cleaned_data['SearchText']
         citys = City.objects.filter(name__contains=SearchText)
    else:
        citys = City.objects.all()
    
    context = {

        "citylist":citys,
        "searchForm": searchForm,

    }

    return render(request, 'Home.html', context)

def comments(request):
    comment = Comment.objects.all()
    context = {'comment': comment}
    return render(request, 'comments.html', context)
    
class City_Name(DetailView):
    model = City
    template_name = 'City.html'

def Restaurant_detail(request, city_id):
    city = City.objects.get(id=city_id)
    restaurants = Restaurants.objects.filter(city=city)

    context = {
        'citys': city,
        'restaurants':restaurants,
    }

    return render(request, 'restaurants_detail.html', context)


def Hotel_detail(request, hotel_id):
    citys = City.objects.get(id=hotel_id)
    hotels = Hotel.objects.filter(city=citys)

    context = {
        'city': citys,
        'hotels':hotels,
    }

    return render(request, 'Hotels_detail.html', context)

def Spectacular_detail(request, spectacular_id):
    city = City.objects.get(id=spectacular_id)
    spectacular = Spectacular_location.objects.filter(city=city)

    context = {
        'city': city,
        'spectacular':spectacular,
    }

    return render(request, 'spectacular_detail.html', context)

class form_restaurant(CreateView):
    model = Restaurants
    form_class = FormRestaurant
    template_name = 'form_restaurants.html'
    success_url = reverse_lazy('home')

class form_comment(CreateView):
    model = Comment
    form_class = FormComment
    template_name = 'form_comment.html'
    success_url = reverse_lazy('home')