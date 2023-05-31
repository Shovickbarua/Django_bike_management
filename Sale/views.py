from django.shortcuts import render,redirect
from Product.models import Product
from Sale.models import Sale
from datetime import datetime
# Create your views here.

def index(request):

    sale = Sale.objects.all()

    return render(request,'sales/sale_list.html',{'sale': sale})

def add(request,id):
    pro= Product.objects.get(id=id)
    return render(request,'sales/add_sale.html',{'pro': pro})


def show_sale(request):
    if 'invoiceID' not in request.session:
        sale =Sale.objects.get(pk=request.session['invoiceID'])
        return render(request,'sales/show_sale.html',{'sale': sale})
    else:
        return redirect(index)
    
def sale_store(request,id):
    
    invoice = Sale.objects.all().order_by('-id').first()
    if invoice == None:
        firstReg = 0
        invoiceID = firstReg+1
        if invoiceID<10:
            id_no = f"{0}{invoiceID}"
        elif invoiceID < 100:
            id_no = invoiceID
    else :
        invoice = Sale.objects.all().order_by('-id').first().id
        invoiceID = invoice+1
        if invoiceID < 10:
            id_no = f"{0}{invoiceID}"
        elif invoiceID < 100:
            id_no = invoiceID
    
    s = request.POST.get('dob')
    d =datetime.strptime(s, "%Y-%m-%d").date()
    years= d.year

    invoiceId = 'HF'+f"{years}{id_no}"

    pro = Product.objects.get(id=id)

    sale = Sale()
    sale.invoiceId =invoiceId
    sale.cus_name =request.POST.get('cus_name')
    sale.method =request.POST.get('method')
    sale.contact =request.POST.get('contact')
    sale.dob =request.POST.get('dob')
    sale.address =request.POST.get('address')
    sale.sale =request.POST.get('sale')
    sale.product_name =pro.product_name
    sale.SKU =pro.SKU
    sale.cat_name =pro.cat.name
    sale.pro_quantity =request.POST.get('pro_quantity')
    sale.cost =pro.cost
    sale.profit =(int(request.POST.get('sale'))*int(request.POST.get('pro_quantity'))) - (int(pro.cost)*int(request.POST.get('pro_quantity')))
    sale.total =int(request.POST.get('sale'))*int(request.POST.get('pro_quantity'))
    sale.save()

    pro.quantity =int(pro.quantity) - int(request.POST.get('pro_quantity'))
    pro.save()

    if 'invoiceID' not in request.session:
        request.session['name'] =invoiceId
        request.session['cus_name'] = request.POST.get('cus_name')
        request.session['method'] = request.POST.get('method')
        request.session['contact'] = request.POST.get('contact')
        request.session['dob'] = request.POST.get('dob')
        request.session['address'] =request.POST.get('address')
    return redirect(index)





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


# Create your views here.
