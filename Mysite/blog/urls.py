from django.urls import path
from .views import blogView , SingleView


urlpatterns = [
   path('home/', blogView, name='blog' ),
   path('single/', SingleView, name='single' ),
]