from django.urls import path
from web.views import HomePage , category , home_type , SingleHome , fileListViews ,FileNewView , my_view, form_comment, UpdateView 

urlpatterns = [
   path('', HomePage,name='home'),
   path('list',fileListViews,name='list'),
   path('category/<str:cat>/', category, name="category"),
   path('category/home-type/<str:pid>/', home_type, name="type-home"),
   path('<int:pid>', SingleHome, name='single' ),
   path('about/', form_comment.as_view(), name='about' ),
   path('file/update/<int:pk>', UpdateView.as_view(), name= 'update'),
   path('file/new', my_view, name= 'home_new'),
]