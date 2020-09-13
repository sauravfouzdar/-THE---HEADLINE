from django.shortcuts import render, get_object_or_404, redirect
from .models import Categories
from django.db import IntegrityError

# Create your views here.


def category_list(request):
    cat = Categories.objects.all()
    return render(request,'back/category_list.html', {'cat':cat})

def add_category(request):   #throwing integrity error 

    if request.method == 'POST':

        name = request.POST.get('name')

        b= Categories(name=name)
        b.save()
        return redirect('category_list')
    return render(request,'back/add_category.html')    
    
def delete_cat(request, pk):

    rmv = Categories.objects.filter(pk=pk)
    rmv.delete()
    
    return redirect('category_list')
    