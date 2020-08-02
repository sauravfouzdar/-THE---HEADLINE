from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
def body_of_news(request, pk):
    
    site = Main.objects.get(pk=2)
    news = News.objects.filter(pk=pk)
    return render(request, 'front/body_of_news.html', {'news':news,'site':site})


def news_list(request):

    news = News.objects.all()
    return render(request, 'back/news_list.html', { 'news':news})


def add_news(request):
  
    if request.method == 'POST':
        titlenews = request.POST.get('titlenews')
        catname = request.POST.get('catname')
        body = request.POST.get('body')

        author = request.POST.get('author')
        timestamp = request.POST.get('timestamp')
        
    #     myfile = request.FILES('myfile')                 #Getting multivalue Dict key is not callable  on myfile
    #     fs = FileSystemStorage()                         #
    #     filename = fs.save(myfile.name, myfile)          #  
    #     url = fs.url(filename)
      
        b = News(Name="Newspaper", 
        title_of_news=titlenews, 
        body_of_news=body, 
        timestamp=timestamp,
        author=author, 
        cat_name=catname,
        cat_id="5", 
        news_view="0")
        b.save()
        return redirect('news_list')
    return render(request, 'back/add_news.html')    

def delete_news(request, pk):

    b=News.objects.filter(pk=pk)
    b.delete()
    
    return redirect('news_list')









