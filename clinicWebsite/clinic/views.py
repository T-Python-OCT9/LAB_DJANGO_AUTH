from django.shortcuts import redirect, render
from django.http import HttpRequest , HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home (request :HttpRequest):
       return render(request  , "clinic/home.html")



def all_doctors(request :HttpRequest):
       if "search" in request.GET:
        all_doctor = Doctor.objects.filter(name__contains=request.GET["search"])
       else:
        all_doctor = Doctor.objects.all()

       return render(request, "clinic/all_doctors.html", {"doctor" : all_doctor})

def add_new_doctor(request :HttpRequest):
    user : User = request.user

    if not (user.is_authenticated and user.has_perm("clinic.add_doctor")):
        return redirect("accounts:login")
    if request.method == "POST":
        new_doctor = Doctor(name=request.POST["name"], description = request.POST["description"], rating=request.POST["rating"], experience_years = request.POST["experience_years"] , specialization=request.POST["specialization"])
        new_doctor.save()
    return render(request  , "clinic/add_doctor.html" )


def list_doctors(request :HttpRequest ):
       if "search" in request.GET:
        details_name = Doctor.objects.filter(name__contains=request.GET["search"])
       else:
        details_name = Doctor.objects.all()

       return render(request, "clinic/doctor_detail.html", {"doctor" : details_name})


def Doctor_detail(request :HttpRequest , Doctor_id : int):
    try:
        doctor = Doctor.objects.get(id=Doctor_id)
    except:
        return render(request , "clinic/home.html")

    return render(request, "clinic/doctor_detail.html", {"doctors" : doctor})


def appointments(request :HttpRequest):
   if request.method == "POST":
        new_appointment = Appointment(patient_name = request.POST ["patient_name"] , case_description = request.POST ["case_description"] ,patient_age = request.POST["patient_age"] ,appointment_datetime = request.POST["appointment_datetime"] , is_attended = request.POST ["is_attended"] )
        new_appointment.save()
        return redirect("clinic:home")
   return render(request , "clinic/appointment.html")

