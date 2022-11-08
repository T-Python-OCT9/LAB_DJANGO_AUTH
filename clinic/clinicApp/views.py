from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import doctor, appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def add_doctor(request : HttpRequest):

    if request.method == "POST":
        new_doctor = doctor(name=request.POST["name"], description = request.POST["description"],  experience_years = request.POST["experience_years"] , rating=request.POST["rating"], image=request.FILES["image"])
        new_doctor.save()
        #specialization=request.POST["specialization"],


    return render(request, "add_doctor.html")

# Create your views here.

def list(request : HttpRequest):

  all_doctors = doctor.objects.all()
  return render(request, 'home.html', {"doctors" : all_doctors})

def doctor_detail(request : HttpRequest, doctor_id : int):

    try:
        doctor = doctor.objects.get(id=doctor_id)
    except:
        return render(request , "not_found.html")

    return render(request, "doctor_detail.html", {"doctor" : doctor})

def list_doctors(request: HttpRequest):

    if "search" in request.GET:
        doctor = doctor.objects.filter(title__contains=request.GET["search"])
    else:
        doctor = doctor.objects.all()

    return render(request, "view_doctors.html", {"doctors" : doctor})


 


