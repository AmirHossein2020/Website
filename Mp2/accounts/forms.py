from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser 



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email','address','phon','post_code')