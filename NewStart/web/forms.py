from django import forms
from .models import Restaurants , Comment

class FormRestaurant(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['name','address','city',
                  'restaurantphoto','description']
        
class SearchForm(forms.Form):
    SearchText=forms.CharField(max_length=100, label="اسم شهر چیه؟", required=False)

class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title','comment','about','date','photo']