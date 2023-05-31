from django.shortcuts import render,redirect
from Product.models import Product
from Category.models import Category
# Create your views here.

def index(request):
    pro = Product.objects.all()

    return render(request,'products/product_list.html',{'pro': pro})

def add(request):
    cat = Category.objects.all()
    return render(request,'products/add_product.html',{'cat':cat})

def store(request):
    pro = Product()
    pro.product_name=request.POST.get('product_name')
    pro.SKU=request.POST.get('SKU')
    pro.dob=request.POST.get('dob')
    pro.quantity=request.POST.get('quantity')
    pro.cost=request.POST.get('cost')
    pro.cat_id=request.POST.get('cat_id')
    pro.pro_image=request.FILES.get('pro_image')
    pro.save()
    
    return redirect(index)

def edit(request,id):
    pro = Product.objects.get(id=id)
    cat = Category.objects.all()
    return render(request,'products/product_edit.html',{'pro': pro,'cat':cat})

def update(request,id):
    pro = Product.objects.get(id=id)
    pro.product_name=request.POST.get('product_name')
    pro.SKU=request.POST.get('SKU')
    pro.dob=request.POST.get('dob')
    pro.quantity=request.POST.get('quantity')
    pro.cost=request.POST.get('cost')
    pro.cat_id=request.POST.get('cat_id')
    pro.pro_image=request.POST.get('pro_image')
    pro.save()
    
    return redirect(index)

def delete(request,id):
    pro = Product.objects.get(id=id)

    pro.delete()
    
    return redirect(index)
