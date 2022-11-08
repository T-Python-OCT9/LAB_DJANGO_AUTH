from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def registerUser(request : HttpRequest):

    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()
        print(new_user)

    return render(request, 'Users/registerUser.html')


def loginUser(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(user)
        
        if user:
            login(request, user)
            return redirect("blogApp:list_posts")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, 'Users/logIn.html', {"msg" : msg})


def logoutUser(request: HttpRequest):

    logout(request)

    return redirect("clinicApp:home")




# Create your views here.
