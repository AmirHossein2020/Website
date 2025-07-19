from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('profileEdit', ProfileEditView, name="profile"),
    path('profile/', user_profile, name='user_profile'),
]