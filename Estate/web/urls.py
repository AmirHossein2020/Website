from django.urls import path
from web.views import HomePage , category , home_type , SingleHome , FileNewView , my_view, form_comment

urlpatterns = [
   path('', HomePage,name='home'),
   path('category/<str:cat>/', category, name="category"),
   path('category/home-type/<str:pid>/', home_type, name="type-home"),
   path('<int:pid>', SingleHome, name='single' ),
   path('about/', form_comment.as_view(), name='about' ),
   path('file/new', my_view, name= 'home_new'),
]