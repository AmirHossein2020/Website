from django.contrib.auth  import authenticate , login , logout 
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
import ticketSales.views
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import *
from accounts.models import ProfileModel
from django.conf import settings
# Create your views here.

def loginView(request):
    #post login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            if request.GET.get('next'):
                return HttpResponseRedirect(reverse(request.GET.get('next')))
            
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                "username": username,
                "errorMessage" : "نام کاربری درست نیست"
            }
            return render(request, 'accounts/login.html',context)
    # gest
    else:
        return render(request, 'accounts/login.html',{})
    
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(ticketSales.views.concertListViews))

@login_required
def profileView(request):
    profile = request.user.profile

    context = {
        "profile":profile
    }

    return render(request, 'accounts/profile.html',context)

def profileRegisterView(request):

    if request.method=="POST":
        profileRegisterForm=ProfileRegisterForm(request.POST,request.FILES)
        if profileRegisterForm.is_valid():

            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                email=profileRegisterForm.cleaned_data['email'],
                                password=profileRegisterForm.cleaned_data['password'],
                                first_name=profileRegisterForm.cleaned_data['first_name'],
                                last_name=profileRegisterForm.cleaned_data['last_name'])

            user.save()

            profileModel=ProfileModel(user=user,
                                       ProfileImage=profileRegisterForm.cleaned_data['ProfileImage'],
                                        Gender=profileRegisterForm.cleaned_data['Gender'],
                                        Credit=profileRegisterForm.cleaned_data['Credit'])

            profileModel.save()

            return HttpResponseRedirect(reverse(ticketSales.views.concertListViews))
    else:
        profileRegisterForm=ProfileRegisterForm()

  
    context={
        "formData":profileRegisterForm
    }


    return render(request,"accounts/profileRegister.html",context)

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
        "ProfileImage":request.user.profile.ProfileImage,
        
    }

    return render(request,"accounts/profileEdit.html",context)