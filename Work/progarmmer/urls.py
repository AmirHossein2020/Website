from django.urls import path ,re_path
from django.conf import settings
from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('resumes/', ResumeView.as_view(), name='resume'),
    path('projects/', ProjectView.as_view(), name='project'),
    path('resume/new', Newresume.as_view(), name='new_resume'),   
    path('project/new', Newproject.as_view(), name='new_project'),
    path('about/', AboutMe.as_view(), name='about'),
    path('persian/', Persian.as_view(), name='persian'),
    path('persian-resumes/', Persian_ResumeView.as_view(), name='persian_resume'),
    path('persian-projects/', Persian_ProjectView.as_view(), name='persian_project'),
    path('persian-about/', Persian_AboutMe.as_view(), name='persian_about'),
]