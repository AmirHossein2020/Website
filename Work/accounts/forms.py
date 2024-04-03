from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser , Contact
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email','age','photo')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']