from django.urls import path
from .views import  ProfileEditView , SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('profileEdit', ProfileEditView, name="profileEdit"),
]