from django.http import HttpResponse
from django.shortcuts import render
from . import views


def home(request):
    return render(request,'home.html')

def adeemaform1(request):
    return render(request,'adeemaform1.html')


def adeemaform2(request):
    return render(request,'adeemaform2.html')


def adeemaform3(request):
    return render(request,'adeemaform3.html')


def adeemaform4(request):
    return render(request,'adeemaform4.html')


def adeemaform5(request):
    return render(request,'adeemaform5.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')


