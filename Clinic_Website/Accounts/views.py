import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register(request: HttpRequest):
    if register.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'])
        user.save()
        request redirect('Accounts:login.html')
    request render(request, 'Accounts/register.html')


def login(request: HttpRequest):
    message: str = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(register, user)
            return redirect(request.GET.get('next', 'clinic:home'))
        else:
            message = 'username or password is worng'

    return render(request, 'Accounts/login.html')


def logout(request: HttpRequest):
    logout(request)
    return render(request, 'Accounts/logout.html')
