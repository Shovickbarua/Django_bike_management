from django.shortcuts import render,redirect
from Category.models import Category
# Create your views here.
def dash(request):

    return render(request,'dashboard/dashboard.html')

def index(request):
    cat = Category.objects.all()
    cat={
        'cat': cat
    }

    return render(request,'categories/cat_list.html',cat)

def add(request):
    
    return render(request,'categories/add_category.html')

def store(request):
    cat = Category()
    cat.name=request.POST.get('name')
    cat.save()
    
    return redirect(index)

def edit(request,id):
    cat = Category.objects.get(id=id)
    cat={
        'cat':cat
    }
    
    return render(request,'categories/cat_edit.html',cat)
   # return render(request,'categories/cat_edit.html',{'cat':cat})

def update(request,id):
    cat = Category.objects.get(id=id)
    cat.name=request.POST.get('name')
    cat.save()
    
    return redirect(index)

def delete(request,id):
    cat = Category.objects.get(id=id)

    cat.delete()
    
    return redirect(index)