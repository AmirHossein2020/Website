from django.shortcuts import render
from django.views.generic import TemplateView , ListView, CreateView
from .models import Resume , Project
from .forms import Formresume , Formproject
from django.urls import reverse_lazy
from accounts.forms import *
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ResumeView(ListView):
    model = Resume
    template_name = 'Resume.html'

class ProjectView(ListView):
    model = Project
    template_name = 'Project.html'



class AboutMe(TemplateView):
    template_name = 'about_me.html'

class Persian(TemplateView):
    template_name = 'Persian/home.html'


class Persian_ResumeView(ListView):
    model = Resume
    template_name = 'Persian/Resume.html'

class Persian_ProjectView(ListView):
    model = Project
    template_name = 'Persian/Project.html'


class Persian_AboutMe(TemplateView):
    template_name = 'Persian/about_me.html'

