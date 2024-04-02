from django.views.generic import TemplateView , ListView 
from .models import Resume , Project , Abuot
from accounts.forms import *
# Create your views here.

class HomeView(TemplateView):
    template_name = 'English/home.html'

class ResumeView(ListView):
    model = Resume
    template_name = 'English/Resume.html'

class ProjectView(ListView):
    model = Project
    template_name = 'English/Project.html'

class AboutMe(TemplateView):
    template_name = 'English/about_me.html'

#=================================================================
#=================================================================
#=================================================================
# this is part of the persian language


class Persian(TemplateView):
    template_name = 'Persian/home.html'


class Persian_ResumeView(ListView):
    model = Resume
    template_name = 'Persian/Resume.html'

class Persian_ProjectView(ListView):
    model = Project
    template_name = 'Persian/Project.html'


class Persian_AboutMe(ListView):
    model = Abuot
    template_name = 'Persian/about_me.html'


