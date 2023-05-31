from django.shortcuts import render,redirect
from Expense.models import Expense
from django.db.models import Sum
# Create your views here.

def index(request):
    ex = Expense.objects.all()

    return render(request,'expenses/expense_list.html',{'ex': ex})

def add(request):
    
    return render(request,'expenses/add_expense.html')

def store(request):
    ex = Expense()
    ex.name=request.POST.get('name')
    ex.dob=request.POST.get('dob')
    ex.amount=request.POST.get('amount')
    ex.save()
    
    return redirect(index)

def edit(request,id):
    ex = Expense.objects.get(id=id)
    
    return render(request,'expenses/expense_edit.html',{'ex': ex})

def update(request,id):
    ex = Expense.objects.get(id=id)
    ex.name=request.POST.get('name')
    ex.dob=request.POST.get('dob')
    ex.amount=request.POST.get('amount')
    ex.save()
    
    return redirect(index)

def delete(request,id):
    ex = Expense.objects.get(id=id)

    ex.delete()
    
    return redirect(index)

def search(request):
    if request.method == 'POST':
        fdob = request.POST.get('fdob')
        ldob = request.POST.get('ldob')      
        ex = Expense.objects.filter(dob__gte=fdob,dob__lte=ldob)
        total = Expense.objects.filter(dob__gte=fdob,dob__lte=ldob).aggregate(Sum('amount'))['amount__sum']

        return render(request,'expenses/expense_bydate.html',{'ex':ex,'total': total})
    else:
        return render(request,'expenses/expense_bydate.html')