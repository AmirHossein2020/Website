from django.urls import path
from .views import  Test, HomeView , AbuotView , contact_view,newsletter_view


urlpatterns = [
   path('', HomeView, name='home' ),
   path('test/', Test, name='test' ),
   path('abuot/', AbuotView, name='about'),
   path('contact/', contact_view, name='contact'),
   path('newsletter/', newsletter_view, name='newsletter'),
]