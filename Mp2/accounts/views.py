from django.shortcuts import render 
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

""" def SignUpView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
    form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form}) """