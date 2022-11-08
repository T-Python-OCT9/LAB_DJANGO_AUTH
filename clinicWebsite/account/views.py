from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register(request : HttpRequest):
    if request.method == "POST":
     new_user = User.objects.create_user(username = request.POST["username"] , email = request.POST["email"] , first_name = request.POST["first_name"], last_name = request.POST["last_name"] , password=request.POST["password"])
     new_user.save()

    return render(request,"account/register.html")

def logIn(request : HttpRequest):
    msg = ""
    if request.method == "post":
        user = authenticate(request , username = request.POST["username"] , password=request.POST["password"])
        if user:
            login(request,user)
            return redirect ("clinic:appointments")
        else:
            msg = "Not Fount , please entre correct username or password"

    return render(request , "account/login.html" , {"msg" : msg})

def logOut(request : HttpRequest):
    logout(request)
    return redirect("clinic:home")