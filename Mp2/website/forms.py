from django import forms
from .models import *

class SearchForm(forms.Form):
    SearchText=forms.CharField(max_length=100, label='Search', required=False)