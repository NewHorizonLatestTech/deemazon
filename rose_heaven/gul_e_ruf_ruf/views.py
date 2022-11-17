from django.http import HttpResponse
from django.shortcuts import render
from . import views


def home(request):
    return render(request,'gul_e_ruf_ruf/home.html')
