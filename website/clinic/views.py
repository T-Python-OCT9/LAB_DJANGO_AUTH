from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Doctor, Appointment
from datetime import datetime
#from .models import Post, Comment

# Create your views here.
def home(request: HttpRequest):

    return render(request, "clinic/homePage.html")

def detailPage(request: HttpRequest):

    return render(request, "clinic/detailPage.html")

def bookingpage(request: HttpRequest):

    return render(request, "clinic/Appointment.html")

def searchBar(request: HttpRequest):

    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])
    else:
        posts = Post.objects.all()


    return render(request, "clinic/detailPage.html", {"posts" : posts})        

def addDoctor(request: HttpRequest):
    specialization_choices = Doctor.specialization_choices
    if request.method == 'POST':
        doctor = Doctor(name=request.POST['name'], description=request.POST['description'], experience_years=request.POST['experience_years'], rating=request.POST['rating'], spcialization =request.POST['spcialization '])
        doctor.save()
    return redirect('clinic:doctors')
    context = {'specialization_choices':specialization_choices}
    return render(request, 'clinic/add.html', context)


def register_user(request : HttpRequest):

    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()

    return render(request, "clinic/register.html")

def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        if user:
            login(request, user)
            return redirect("clinic:home")
        else:
            msg = "User Not Found , check your username and password "

    return render(request, "clinic/login.html", {"msg" : msg})


def logout_user(request: HttpRequest):

    logout(request)

    return redirect("clinic:home")

