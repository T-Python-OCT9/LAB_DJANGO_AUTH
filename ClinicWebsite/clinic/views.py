from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor, Appointment

# Create your views here.



def home_page (request : HttpRequest):

    return render(request, "clinic/home_page.html")

def error_page (request : HttpRequest):

    return render(request, "clinic/not_found.html")


def list_doctors(request: HttpRequest):

    if "search" in request.GET:
        doctors = Doctor.objects.filter(name__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()

    return render(request, "clinic/list_doctors.html", {"doctors": doctors})


def detail_page(request : HttpRequest, doc_id: int):

    try:
        doctor= Doctor.objects.get(id=doc_id)
        appointment = Appointment.objects.filter(doctor = doctor)

    except:
        return render(request, "clinic/not_found.html")

    return render(request, "clinic/detail_page.html", {"doctor": doctor, "appointments": appointment})


def make_appointment(request : HttpRequest, doc_id: int):

    doctor = Doctor.objects.get(id= doc_id)

    if request.method == "POST":
        new_appointment = Appointment(doctor = doctor, patient_name= request.POST["patient_name"], case_description = request.POST["case_description"], patient_age = request.POST["patient_age"], appointment_datetime = request.POST["appointment_datetime"], is_attended = request.POST["is_attended"])
        new_appointment.save()
    

    return redirect("clinic:detail_page", doctor.id)


def add_doctor(request: HttpRequest):
    
    if request.user.has_perm("clinic.delete_doctor"):
        if request.method == "POST":
            new_doctor = Doctor(name= request.POST["name"], description = request.POST["description"],
                specialization = request.POST["specialization"],experience_years = request.POST["experience_years"],
                rating = request.POST["rating"])
            new_doctor.save()
    else:
        return redirect('clinic:home_page')

    return render(request, "clinic/add_doc.html")

