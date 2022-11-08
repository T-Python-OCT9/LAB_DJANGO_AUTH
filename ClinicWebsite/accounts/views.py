from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registerPage(request: HttpRequest):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'])
        user.save()
        return redirect('accounts:login_user')
    return render(request, 'accounts/register.html')

def loginPage(request: HttpRequest):
    message: str = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'clinic:home'))
        else:
            message = 'Username or Password is worng!'
    return render(request, 'accounts/login.html', {'message':message})

def logoutPage(request: HttpRequest):
    logout(request)
    return render(request, 'accounts/logout.html')