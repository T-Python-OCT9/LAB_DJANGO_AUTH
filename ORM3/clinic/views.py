from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor, Appointment

# Create your views here.

def add_doctor(request : HttpRequest):
  
    if request.method == "POST":
        new_Doctors = Doctor(name=request.POST["name"], description = request.POST["description"], spec=request.POST["spec"], experience_years = request.POST["experience_years"],rating=request.POST["rating"])
        new_Doctors.save()

    return render(request, "clinic/add_doctor.html")

def list_doctors(request: HttpRequest):


    if "search" in request.GET:
        doctors = Doctor.objects.filter(title__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()


    return render(request, "clinic/view_doctor.html", {"doctors" : doctors})



def doctors_detail(request : HttpRequest, doctor_id : int):

    try:
        doctors = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctors = doctors)
    except:
        return render(request , "clinic/not_found.html")

    return render(request, "clinic/detail.html", {"doctors" : appointments, "appointments" : appointments})




