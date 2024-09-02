from django.urls import path
from .views import *


urlpatterns = [
   path('home/', blogView, name='blog' ),
   path('<int:pid>', SingleView, name='single' ),
   path('author/<str:author_username>', blogView, name='author' ),
   path('search/', blog_search, name='search' ),
   path('category/<str:cat_name>', blog_category, name='category' ),
]