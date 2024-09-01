from django.urls import path
from web.views import HomePage , category , home_type , SingleHome , FileNewView , vew , my_view

urlpatterns = [
   path('', HomePage,name='home'),
   path('category/<str:cat>/', category, name="category"),
   path('category/home-type/<str:pid>/', home_type, name="type-home"),
   path('<int:pid>', SingleHome, name='single' ),
   path('file/new', my_view, name= 'home_new'),
]