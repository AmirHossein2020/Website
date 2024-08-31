from django.urls import path
from .views import blogView , SingleView , blog_category


urlpatterns = [
   path('home/', blogView, name='blog' ),
   path('<int:pid>', SingleView, name='single' ),
   path('category/<str:cat_name>', blog_category, name='category' ),
]