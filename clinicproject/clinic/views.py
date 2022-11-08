from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Doctor, Appointment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request:HttpRequest):
    
    return render(request, 'clinic/base.html')


def add_doctor(request:HttpRequest):
    if request.method == "POST":
        new_doctor = Doctor(name=request.POST.get('name'), description= request.POST.get('description'),specialization = request.POST.get('specialization') ,experience_years= request.POST.get('experience_years'),rating= request.POST.get('rating'))
        new_doctor.save()

    return render(request, "clinic/add_doctors.html",{"Doctor" : Doctor})


def doctors(request:HttpRequest):

    if "search" in request.GET:
        doctors = Doctor.objects.filter(name__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()

    return render(request, "clinic/list_doctors.html", {"doctors" : doctors})


def view_doctor(request:HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctor = doctor)
    except:
        return render(request, "clinic/not_found.html")

    context = {'doctor': doctor, 'appointments': appointments}
    return render(request, "clinic/view_doctor.html", context)


def appointment(request:HttpRequest, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)

    return render(request, "clinic/appointment.html",{'doctor': doctor})


def add_appointment(request:HttpRequest, doctor_id: int):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == "POST":
        new_appointment = Appointment(doctor=doctor,pationt_name=request.POST.get('pationt_name'), case_description= request.POST.get('case_description'),patient_age = request.POST.get('patient_age') ,appointment_datetime= request.POST.get('appointment_datetime'),is_attended= request.POST.get('is_attended'))
        new_appointment.save()


    return redirect("clinic:view_doctor", doctor.id)


def update_doctor(request: HttpRequest, doctor_id:int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request, "clinic/not_found.html")
    else:
        if request.method == 'POST':
            doctor.name = request.POST.get('name')
            doctor.description = request.POST.get('description')
            doctor.specialization = request.POST.get('specialization')
            doctor.experience_years = request.POST.get('experience_years')
            doctor.rating = request.POST.get('rating')
            post.save()

            return redirect("clinic:list_doctors")

        return render(request, "clinic/update_doctor.html",{'doctor': doctor})