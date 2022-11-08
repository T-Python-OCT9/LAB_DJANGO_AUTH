from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import redirect, render
from .models import Doctor,Appointment
# Create your views here.


def home(request : HttpRequest):
    doctors=Doctor.objects.all()
    return render(request, "ClincApp/home.html", {"doctor" : doctors})


def viwe_details(request : HttpRequest, d_id : int):

        doctor = Doctor.objects.get(id=d_id)
        appointment = Appointment.objects.filter(doctor=doctor)
        
        return render(request, "ClincApp/detials.html", {"doctor" : doctor,"appointments" : appointment})

def add(request : HttpRequest):
    user : User = request.user

    if not (user.is_authenticated and user.has_perm("ClincApp.admin")):
        return redirect("accounts:login_user")
    if request.method=="POST":
        new_doctor=Doctor(name=request.POST['name'], description=request.POST['description'], specialization=request.POST['choise'], experience_years=3, rating=2)
        new_doctor.save()
    return render(request, "ClincApp/admin.html")


def search(request:HttpRequest):
    if 'search' in request.GET:
        doctor = Doctor.objects.filter(name__contains = request.GET['search'] )
    else:
        doctor = Doctor.objects.all()
    context={"doctor" : doctor}
    return render(request, "ClincApp/search.html" , context )


def book_abiontment(request: HttpRequest, doctor_id:int):
    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == "POST":
        new_appointment = Appointment(doctor=doctor, patient_name= request.POST["name"], case_description=" ",patient_age=request.POST["patient_age"],appointment_datetime=request.POST["appointment_datetime"], is_attended=True ,doctor_id= doctor_id)
        new_appointment.save()

    
    return redirect("ClincApp:viwe_details", doctor.id)
