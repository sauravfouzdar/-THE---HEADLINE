from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Main
from news.models import News


def home(request):
    
    site = Main.objects.get(pk=2)
    news = News.objects.all()  #imported News model from news app
    return render(request, 'front/home.html', {'site':site, 'news':news})
   
def about(request):

    site = Main.objects.get(pk=2)
    return render(request, 'front/about.html', {'site':site})

def panel(request):
    return render(request, 'back/home.html')    


def business(request):
    return render(request, 'front/business.htm')  

def sports(request):
    return render(request, 'front/sports.htm')  

def science(request):
    return render(request, 'front/science.htm') 












