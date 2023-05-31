from django.shortcuts import render,redirect
from Income.models import Income
from django.db.models import Sum
# Create your views here.

def index(request):
    income = Income.objects.all()

    return render(request,'incomes/income_list.html',{'income': income})

def add(request):
    
    return render(request,'incomes/add_income.html')

def store(request):
    income = Income()
    income.name=request.POST.get('name')
    income.dob=request.POST.get('dob')
    income.amount=request.POST.get('amount')
    income.save()
    
    return redirect(index)

def edit(request,id):
    income = Income.objects.get(id=id)
    
    return render(request,'incomes/income_edit.html',{'income': income})

def update(request,id):
    income = Income.objects.get(id=id)
    income.name=request.POST.get('name')
    income.dob=request.POST.get('dob')
    income.amount=request.POST.get('amount')
    income.save()
    
    return redirect(index)

def delete(request,id):
    income = Income.objects.get(id=id)

    income.delete()
    
    return redirect(index)


def search(request):
    if request.method =="POST":
        fdob = request.POST.get('fdob')
        ldob = request.POST.get('ldob')
        income = Income.objects.filter(dob__gte=fdob,dob__lte=ldob)
        total = Income.objects.filter(dob__gte=fdob,dob__lte=ldob).aggregate(Sum('amount'))['amount__sum']

        return render(request,'incomes/income_bydate.html',{'income': income, 'total': total})
    else:
        return render(request,'incomes/income_bydate.html')