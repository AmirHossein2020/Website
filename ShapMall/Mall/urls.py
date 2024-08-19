"""
URL configuration for Mall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#================================================================================================
# متصل میشه html در این قسمت ما صفحه های سایت و ادرس دهی میکنیم
# تا عمل های که برای هر صفحه انجام میدیم 
# انجام بشه درواقعه با ادرس دهی که اینجا انجام میدیم به صفحه های  


from django.contrib import admin
from django.urls import path , include
from shop.views import *
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('cart/', include('cart.urls')),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
