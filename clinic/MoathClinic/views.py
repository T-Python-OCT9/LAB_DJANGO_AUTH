from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor,Appointment
# Create your views here.

def Gallery(request:HttpRequest):

    return render(request,"MoathClinic/gallery.html")

def Home_Page(request:HttpRequest):

    return render(request,"MoathClinic/base.html")

def add_Doctors(request:HttpRequest):
    if request.method == "POST":
        new_Doctors = Doctor (name=request.POST["name"], description = request.POST["description"], specialization=request.POST["specialization"], experience_years = request.POST["experience_years"],rating=request.POST["rating"])
        new_Doctors.save()

    return render(request,"MoathClinic/add_doctors.html")

def list_doctors(request: HttpRequest):

    if "search" in request.GET:
        doctors = Doctor.objects.filter(name__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()

    return render(request, "MoathClinic/view_doctors.html", {"doctors" : doctors})



def doctor_detail(request : HttpRequest, doctor_id : int):

    try:
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctor = doctor)
    except:
        return render(request , "MoathClinic/not_found.html")

    return render(request, "MoathClinic/detail_doctor.html", {"doctor" : doctor, "appointments" : appointments})



def update_doctor(request: HttpRequest, doctor_id:int):

    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request , "MoathClinic/not_found.html")

    if request.method == "POST":
        doctor.name = request.POST["name"]
        doctor.description = request.POST["description"]
        doctor.specialization = request.POST["specialization"]
        doctor.experience_years = request.POST["experience_years"]
        doctor.rating = request.POST["rating"]
        doctor.save()

        return redirect("MoathClinic:list_doctors")


    return render(request, "MoathClinic/update_doctor.html", {"doctor" : doctor})



def delete_doctor(request: HttpRequest, doctor_id:int):

    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request , "MoathClinic/not_found.html")

    doctor.delete()

    return redirect("MoathClinic:list_doctors")




def add_appointment(request: HttpRequest, doctor_id:int):
    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == "POST":
        new_appointment = Appointment(doctor=doctor, patient_name = request.POST["patient_name"], case_description=request.POST["case_description"], patient_age = request.POST["patient_age"], appointment_datetime=request.POST["appointment_datetime"], is_attended=request.POST["is_attended"] )
        new_appointment.save()

    return redirect("ClinicApp:doctor_detail", doctor.id)    