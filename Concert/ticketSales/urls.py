from django.urls import path
from ticketSales.views import *

urlpatterns = [
    path('concert/list',concertListViews),
    path('location/list',locationListViews),
    path('concert/<int:concert_id>',concertDetailsViews),
    path('time/list',timeViews),
    path('concertEdit/<int:concert_id>', concertEditView)
]