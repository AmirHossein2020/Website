from django.urls import path
from .views import HomeView , AbuotView , ContactView


urlpatterns = [
   path('', HomeView, name='home' ),
   path('abuot/', AbuotView, name='about'),
   path('contact/', ContactView, name='contact')
]