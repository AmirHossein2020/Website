from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser 
from django import forms



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email','address','phon','post_code')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['address','phon','post_code']


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields=["first_name","last_name","email"]
    password=None