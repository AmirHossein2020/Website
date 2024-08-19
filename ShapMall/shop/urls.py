# در اینجا هم ادرس ویوی که درست کردیم میدیم
# تا جنگو با این ادرس ویوی مارو نشون بده
from django.urls import path , include
from .views import *

urlpatterns = [
    path('', helloworld, name="home"),
    path('about/', about, name="about"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('signup', signup_user, name="signup"),
    path('product/<int:pk>/', product, name="product"),
    path('category/<str:cat>/', category, name="category"),
    path('category/', category_summary, name="category_summary"),
]
