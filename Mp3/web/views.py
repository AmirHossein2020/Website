from django.shortcuts import render
from web.models import *
from accounts.models import *

# Create your views here.

def home(request):
    ProductAll = Products.objects.all()
    context = {
        'proall':ProductAll,
    }
    return render(request, 'index.html' , context)

def profile(request):
    # مطمئن شوید که کاربر لاگین کرده باشد و request.user معتبر است.
    # در غیر این صورت، این خط ممکن است خطا بدهد اگر request.user یک کاربر ناشناس باشد.
    # می‌توانید یک شرط برای بررسی لاگین بودن کاربر اضافه کنید:
    if request.user.is_authenticated:
        profile_user = CustomUser.objects.get(id=request.user.id)
        context = {
            'profile': profile_user
        }
        return render(request, 'Profile.html', context)
    else:
        # اگر کاربر لاگین نکرده باشد، می‌توانید او را به صفحه لاگین ریدایرکت کنید
        # یا یک پیغام خطا نمایش دهید.
        # مثال:
        # from django.shortcuts import redirect
        # return redirect('login') # فرض کنید یک URL به نام 'login' دارید
        return render(request, 'Profile.html', {'profile': None, 'message': 'Please log in to view your profile.'})


def about(request):
    return render(request, 'about.html')

def client(request):
    return render(request, 'client.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    PAll = Products.objects.all()
    context = {
        'proall':PAll,
    }
    return render(request, 'products.html',context)

def product(request, pk):
    product = Products.objects.get(id=pk)
    return render(request, 'singl.html', {'product': product})





