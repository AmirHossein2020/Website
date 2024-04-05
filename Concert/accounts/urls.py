from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', loginView),
    path('logout/', logoutView),
    path('profile/', profileView),
    path('profileRegister/', profileRegisterView),
    path('profileEdit', ProfileEditView),
]