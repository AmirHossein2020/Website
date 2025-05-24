from django.shortcuts import render 
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def ProfileEditView(request):
    
    if request.method=="POST":
        profileEditForm=ProfileEditForm(request.POST,request.FILES, instance=request.user.profile)
        userEditForm=UserEditForm(request.POST,instance=request.user)
        if profileEditForm.is_valid and userEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse(profileView))
    else:
        profileEditForm=ProfileEditForm(instance=request.user.profile)
        userEditForm=UserEditForm(instance=request.user)

    context={

        "profileEditForm":profileEditForm,
        "userEditForm":userEditForm,
        
    }

    return render(request,"template/profileEdit.html",context)





""" def SignUpView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
    form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form}) """
