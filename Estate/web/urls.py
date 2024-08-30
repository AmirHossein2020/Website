from django.urls import path
from web.views import HomePage , category , home_type

urlpatterns = [
   path('', HomePage,name='home'),
   path('category/<str:cat>/', category, name="category"),
   path('category/home-type/<str:pid>/', home_type, name="type-home"),
]