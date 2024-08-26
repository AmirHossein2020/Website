from django.urls import path , include
from web.views import Restaurant_detail, Hotel_detail, Spectacular_detail ,City_Name, comments, HomeView , form_restaurant , form_comment


urlpatterns = [
    path('', HomeView, name='home'),
    path('explor/', comments, name='explor'),
    path('city/<int:pk>', City_Name.as_view(), name='city_name'),
    path('city/spectacular/<int:spectacular_id>', Spectacular_detail, name='spectacular_detail'),
    path('city/hotel/<int:hotel_id>', Hotel_detail, name='hotel_detail'),
    path('city/city/<int:city_id>', Restaurant_detail, name='city_detail'),
    path('restaurant/new', form_restaurant.as_view(), name='new_restaurant'),
    path('comment', form_comment.as_view(), name='comment'),
]