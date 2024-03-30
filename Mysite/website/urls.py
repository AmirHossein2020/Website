from django.urls import path
from .views import HomeView , AbuotView


urlpatterns = [
   path('', HomeView, name='home' ),
   path('abuot/', AbuotView, name='abuot')
]