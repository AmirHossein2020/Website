from django.urls import path
from web.views import HomePage , category , category_type

urlpatterns = [
   path('', HomePage,name='home'),
   path('category/<str:cat>/', category, name="category"),
   path('cat/<str:pid>', category_type, name="category_type"),
]