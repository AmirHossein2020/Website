from django import forms
from web.models import HomeFile
from django.contrib.auth.models import User

class PostFile(forms.ModelForm):
    class Meta:
        model = HomeFile
        fields = ['model', 'type', 'meterage', 'rooms',
                  'bathroom', 'wc', 'mortage_price', 'rental_price',
                  'selling_price', 'address', 'about', 'phonehome', 'image',
                  'image2', 'image3', 'image4', 'author']

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with the given user as the author if provided.
        
        Pop the 'user' keyword argument from the kwargs and use it to set the
        initial value of the 'author' field. If no user is provided, just call
        the parent's __init__ method.
        """
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.initial['author'] = user
        self.fields['author'].widget = forms.HiddenInput()

