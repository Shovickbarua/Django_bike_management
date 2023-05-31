from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def loginpage(request):

    return render(request,'login.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dash')
        else:
            # No backend authenticated the credentials
            return redirect(loginpage)
def signout(request):
    logout(request)
    return redirect(loginpage)