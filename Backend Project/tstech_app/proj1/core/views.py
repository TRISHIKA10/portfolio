from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
# Create your views here.

def homePage(request):
    context = {
        "title":"Welcome to TSTech"
    }
    return render(request,"homePage.html", context)

def aboutUs(request):
    context = {
        "title":"About TSTech"
    }
    return render(request,"aboutUs.html", context)

def ourServices(request):
    context = {
        "title":"TsTech Services"
    }
    return render(request,"ourServices.html", context)
def contactUs(request):
    context = {
        "title":"contact Us"
    }
    return render(request,"contactUs.html", context) 
# def contactUs(request):
#     return HttpResponse("Welcome to tstech") 

