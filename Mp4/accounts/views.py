from django.shortcuts import render 
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def ProfileEditView(request):
    
    if request.method=="POST":
        profileEditForm=ProfileEditForm(request.POST,request.FILES, instance=request.user)
        userEditForm=UserEditForm(request.POST,instance=request.user)
        if profileEditForm.is_valid and userEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        profileEditForm=ProfileEditForm(instance=request.user)
        userEditForm=UserEditForm(instance=request.user)

    context={

        "profileEditForm":profileEditForm,
        "userEditForm":userEditForm,
        
    }

    return render(request,"registration/profileEdit.html",context)


@login_required
def user_profile(request):
    user = request.user
    return render(request, 'registration/user_profile.html', {'user': user})


""" def SignUpView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
    form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form}) """