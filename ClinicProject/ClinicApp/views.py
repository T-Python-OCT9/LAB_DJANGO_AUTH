from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor, Appointment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
#---------------ADD NEW DOCTOR------------

def add_doctor(request : HttpRequest):
    user : User = request.user

    if not (user.is_authenticated and  user.has_perm("ClinicApp.add_doctor")):
        return redirect("accounts:login_user")

    if request.method == "POST":
        new_doctor = Doctor(user = user , image=request.FILES["image"], name=request.POST["name"], description = request.POST["description"], specialization=request.POST["specialization"], experience_years = request.POST["experience_years"], rating = request.POST["rating"])
        new_doctor.save()


    return render(request, "ClinicApp/add_doctor.html")


#---------------LIST ALL DOCTORS------------
def list_doctors(request: HttpRequest):

    if "search" in request.GET:
        doctors = Doctor.objects.filter(name__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()

    return render(request, "ClinicApp/view_doctors.html", {"doctors" : doctors })


#---------------DOCTORS' DETAILS------------
def doctor_detail(request : HttpRequest, doctor_id : int):

    try:
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctor = doctor)
    except:
        return render(request , "ClinicApp/not_found.html")

    return render(request, "ClinicApp/doctor_detail.html", {"doctor" : doctor, "appointments" : appointments})


#---------------UPDATE DOCTOR------------
@login_required
def update_doctor(request: HttpRequest, doctor_id:int):
    user : User = request.user

    if not user.has_perm("ClinicApp.change_doctor"):
        return redirect("accounts:login_user")

    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request , "ClinicApp/not_found.html")

    if request.method == "POST":
        user = user 
        doctor.name = request.POST["name"]
        doctor.description = request.POST["description"]
        doctor.specialization = request.POST["specialization"]
        doctor.experience_years = request.POST["experience_years"]
        doctor.rating = request.POST["rating"]
        doctor.image = request.FILES["image"]
        doctor.save()

        return redirect("ClinicApp:list_doctors")

    
    return render(request, "ClinicApp/update_doctor.html", {"doctor" : doctor})


#---------------DELETE DOCTOR------------
def delete_doctor(request: HttpRequest, doctor_id:int):

    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request , "ClinicApp/not_found.html")

    doctor.delete()

    return redirect("ClinicApp:list_doctors")



#---------------ADD APPOINTMENT------------
def add_appointment(request: HttpRequest, doctor_id:int):
    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == "POST":
        new_appointment = Appointment(doctor=doctor, patient_name = request.POST["patient_name"], case_description=request.POST["case_description"], patient_age = request.POST["patient_age"], appointment_datetime=request.POST["appointment_datetime"], is_attended=request.POST["is_attended"] )
        new_appointment.save()
    
    return redirect("ClinicApp:doctor_detail", doctor.id)