from django.urls import path 
from website.views import home
from website import views

urlpatterns = [
    path('', views.home, name='home'),
]