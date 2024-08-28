from django.urls import path
from web.views import HomePage

urlpatterns = [
   path('', HomePage,name='home'),
]