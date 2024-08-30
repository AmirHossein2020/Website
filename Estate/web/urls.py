from django.urls import path
from web.views import HomePage , category , category2

urlpatterns = [
   path('', HomePage,name='home'),
   path('category/<str:cat>/', category, name="category"),

]