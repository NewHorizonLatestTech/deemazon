"""rose_heaven URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('adeemaform1/', views.adeemaform1, name='adeemaform1'),
    path('adeemaform2/', views.adeemaform2, name='adeemaform2'),
    path('adeemaform3/', views.adeemaform3, name='adeemaform3'),
    path('adeemaform4/', views.adeemaform4, name='adeemaform4'),
    path('adeemaform5/', views.adeemaform5, name='adeemaform5'),
    path('contact/', views.contact, name='contact'),
    path('gul_e_baad/', include('gul_e_baad.urls')),
    path('gul_e_ruf_ruf/', include('gul_e_ruf_ruf.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))