from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('contact/', ContactView.as_view(), name= 'contact'),
    path('persian_contact/', Persian_ContactView.as_view(), name= 'persian_contact'),
]