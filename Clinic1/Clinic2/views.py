from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor, Appointment
from .doctors import Doctors

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here. 

doctor1 = Doctors("Ahmad", "Doctor specializing in Neurology", "Nerves",10 , 5)
doctor2 = Doctors("Sara", "Specialized in skin diseases and the conduct of surgical and non-surgical operations", "Skin diseases",7 , 5)
doctor3 = Doctors("Nora", "Diagnosis and treatment of childhood diseases", "Pediatric",7 , 4)
doctor4 = Doctors("Mohamad", "Specialist in Psychiatry", "Psychiatric illness",6 , 4)

list = [doctor1, doctor2, doctor3, doctor4]



def Home(request : HttpRequest):
    
    limit = int(request.GET.get("limit", 5))

    output = " "

    for doc in list[:limit]:
        output += doc.getName()
        
        
    return render(request, "Clinic2/Home.html",{"list" : output})


def detail(request : HttpRequest):

    context = {
        "doctor1" :  ["Ahmad", "Doctor specializing in Neurology", "Nerves", 10, 5] , 
        "doctor2": ["Sara", "Specialized in skin diseases and the conduct of surgical and non-surgical operations", "Skin diseases", 7, 5],
        "doctor3" : ["Nora", "Diagnosis and treatment of childhood diseases", "Pediatric", 7, 4],
        "doctor4" : ["Mohamad", "Specialist in Psychiatry", "Psychiatric illness", 6, 4],
        }

    return render(request, "Clinic2/detail.html", context )






#Lab AUTH

def register(request : HttpRequest):

    if request.method == "POST":

       NUser = User.objects.create_user( username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"],email= request.POST["email"], password=request.POST["password"])
       NUser.save()

    return render(request, "Clinic2/register.html") 


def login(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user is not None:
            login(request, user)
            return redirect("Clinic2:Home")
        else:
            msg = "Sorry"

    return render(request, "Clinic2/login.html", {"msg" : msg})   


def logout(request: HttpRequest):

    logout(request)

    return redirect("Clinic2:Home")    


def limit(request: HttpRequest):
    if request.user.is_authenticated:
        return render(request, 'Clinic2/detail.html')      