from django.shortcuts import render,redirect
from Bikesale.models import bikesale
from Bikeservice.models import Bikeservice
from Bike.models import Bike
from datetime import datetime,timedelta
# Create your views here.

def index(request):
    bike = bikesale.objects.all()

    return render(request,'bikes/bike_sale_list.html',{'bike': bike})

def add(request,id):
    bike = Bike.objects.get(id=id)

    return render(request,'bikes/add_order.html',{'bike': bike})

def store(request,id):
            
    invoice = bikesale.objects.all().order_by('-id').first()

    if invoice == None:
        firstReg = 0
        invoiceID = firstReg+1
        if invoiceID<10:
            id_no = f"{0}{invoiceID}"
        elif invoiceID < 100:
            id_no = invoiceID
    else :
        invoice = bikesale.objects.all().order_by('-id').first().id
        invoiceID = invoice+1
        if invoiceID < 10:
            id_no = f"{0}{invoiceID}"
        elif invoiceID < 100:
            id_no = invoiceID

    s = request.POST.get('dob')
    d =datetime.strptime(s, "%Y-%m-%d").date()
    years= d.year

    invoiceId = 'HF'+f"{years}{id_no}"

    bikes = Bike.objects.get(id=id)

    bike = bikesale()
    bike.invoiceId=invoiceId
    bike.client_name=request.POST.get('client_name')
    bike.fname=request.POST.get('fname')
    bike.nid=request.POST.get('nid')
    bike.method=request.POST.get('method')
    bike.contact=request.POST.get('contact')
    bike.address=request.POST.get('address')
    bike.brand=bikes.brand
    bike.bike_name=bikes.bike_name
    bike.bsquantity=request.POST.get('bsquantity')
    bike.dob=request.POST.get('dob')
    bike.bcost=bikes.bcost
    bike.color=request.POST.get('color')
    bike.engine_no=bikes.engine_no
    bike.chas_no=bikes.chas_no
    bike.m_veh=bikes.m_veh
    bike.manu=bikes.manu
    bike.cc=bikes.cc
    bike.seat_cap=bikes.seat_cap
    bike.brake=bikes.brake
    bike.ftyre=bikes.ftyre
    bike.rtyre=bikes.rtyre
    bike.weight=bikes.weight
    bike.sale_price=request.POST.get('sale_price')
    bike.registration=request.POST.get('registration')
    bike.bank_draft=request.POST.get('bank_draft')
    bike.brta=request.POST.get('bank_draft')
    bike.profit=(int(request.POST.get('sale_price')) * int(request.POST.get('bsquantity')))
    bike.total=(int(request.POST.get('sale_price')) * int(request.POST.get('bsquantity')))+int(request.POST.get('registration'))+int(request.POST.get('bank_draft'))+int(request.POST.get('bank_draft'))
    bike.cus_photo=request.FILES.get('cus_photo')
    bike.b_copy=request.FILES.get('b_copy')
    bike.r_slip=request.FILES.get('r_slip')
    bike.t_token=request.FILES.get('t_token')
    bike.save()


    bikes.bquantity = int(bikes.bquantity) - int(request.POST.get('bsquantity'))
    bikes.save()

    service = Bikeservice()
    service.invoiceId=invoiceId
    service.client_name=request.POST.get('client_name')
    service.contact=request.POST.get('contact')
    service.address=request.POST.get('address')
    service.service_type='first'
    service.first_service     =d + timedelta(days=10)
    service.second_service    =d + timedelta(days=35)
    service.third_service     =d + timedelta(days=140)
    service.fourth_service    =d + timedelta(days=200)
    service.fifth_service     =d + timedelta(days=260)
    service.sixth_service     =d + timedelta(days=320)
    service.seventh_service   =d + timedelta(days=380)
    service.eighth_service    =d + timedelta(days=440)
    service.save()
    
    return redirect(index)

def edit(request,id):
    bike = bikesale.objects.get(id=id)
    return render(request,'bikes/bike_edit.html',{'bike': bike})

def update(request,id):
    bike = bikesale.objects.get(id=id)
    bike.invoiceId=request.POST.get('invoiceId')
    bike.client_name=request.POST.get('client_name')
    bike.fname=request.POST.get('fname')
    bike.nid=request.POST.get('nid')
    bike.method=request.POST.get('method')
    bike.contact=request.POST.get('contact')
    bike.address=request.POST.get('address')
    bike.brand=request.POST.get('brand')
    bike.bike_name=request.POST.get('bike_name')
    bike.bsquantity=request.POST.get('bsquantity')
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
    bike.sale_price=request.POST.get('sale_price')
    bike.bank_draft=request.POST.get('bank_draft')
    bike.brta=request.POST.get('brta')
    bike.profit=request.POST.get('profit')
    bike.total=request.POST.get('total')
    bike.cus_photo=request.Files.get('cus_photo')
    bike.b_copy=request.POST.get('b_copy')
    bike.r_slip=request.POST.get('r_slip')
    bike.t_token=request.POST.get('t_token')
    bike.save()
    
    return redirect(index)

def delete(request,id):
    bike = bikesale.objects.get(id=id)

    bike.delete()
    
    return redirect(index)

