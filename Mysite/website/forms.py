from django import forms
from website.models import Contact , Newsletter
class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailInput()
    subject = forms.CharField(max_length=255)
    massage = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('__all__')


class Newsletterform(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ('__all__')