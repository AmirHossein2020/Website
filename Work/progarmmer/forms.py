from django import forms
from .models import Resume , Project

class Formresume(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['experiencename','aboutexperience',
        'startyear','endyear','nameinstitute',
        'startyear_education','endyear_education',
        'namecity', 'abuotinstitute',
        'professional_skill','language']

class Formproject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['nameproject','abuotproject','photoproject']