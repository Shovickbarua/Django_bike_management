from django.shortcuts import render,redirect
from Bike.models import Bike
# Create your views here.

def index(request):
    bike = Bike.objects.all()

    return render(request,'bikes/bike_list.html',{'bike': bike})

def add(request):

    return render(request,'bikes/add_bike.html')

def store(request):
    bike = Bike()
    bike.brand=request.POST.get('brand')
    bike.bike_name=request.POST.get('bike_name')
    bike.bquantity=request.POST.get('bquantity')
    bike.dob=request.POST.get('dob')
    bike.bcost=request.POST.get('bcost')
    bike.color=request.POST.get('color')
    bike.engine_no=request.POST.get('engine_no')
    bike.chas_no=request.POST.get('chas_no')
    bike.m_veh=request.POST.get('m_veh')
    bike.manu=request.POST.get('manu')
    bike.cc=request.POST.get('cc')
    bike.seat_cap=request.POST.get('seat_cap')
    bike.brake=request.POST.get('brake')
    bike.ftyre=request.POST.get('ftyre')
    bike.rtyre=request.POST.get('rtyre')
    bike.weight=request.POST.get('weight')
    bike.bike_image=request.FILES.get('bike_image')
    bike.save()
    
    return redirect(index)

def edit(request,id):
    bike = Bike.objects.get(id=id)
    return render(request,'bikes/bike_edit.html',{'bike': bike})

def update(request,id):
    bike = Bike.objects.get(id=id)
    bike.brand=request.POST.get('brand')
    bike.bike_name=request.POST.get('bike_name')
    bike.bquantity=request.POST.get('bquantity')
    bike.dob=request.POST.get('dob')
    bike.bcost=request.POST.get('bcost')
    bike.color=request.POST.get('color')
    bike.engine_no=request.POST.get('engine_no')
    bike.chas_no=request.POST.get('chas_no')
    bike.m_veh=request.POST.get('m_veh')
    bike.manu=request.POST.get('manu')
    bike.cc=request.POST.get('cc')
    bike.seat_cap=request.POST.get('seat_cap')
    bike.brake=request.POST.get('brake')
    bike.ftyre=request.POST.get('ftyre')
    bike.rtyre=request.POST.get('rtyre')
    bike.weight=request.POST.get('weight')
    bike.bike_image=request.FILES.get('bike_image')
    bike.save()
    
    return redirect(index)

def delete(request,id):
    bike = Bike.objects.get(id=id)

    bike.delete()
    
    return redirect(index)
