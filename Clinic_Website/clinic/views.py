from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Doctor , Appointment


# Create your views here.
def home(request : HttpResponse):
    try:
        if "search" in request.GET:
            doctors = Doctor.objects.filter(name__contains=request.GET["search"])
        else:
            doctors =  Doctor.objects.all()
    except:
        return render(request , "clinic/not_found.html")
    
    return render(request,"clinic/home.html",{"doctors":doctors})



def add_doctor(request : HttpResponse):
    if request.method == "POST":
        new_book = Doctor(name=request.POST["name"], description= request.POST["description"],
         specialization= request.POST["specialization"] , experience_years= request.POST["experience_years"]
         , rating= request.POST["rating"])
        new_book.save()
        return redirect("clinic:home")

    return render(request,"clinic/add_doctor.html")



def detail_doctor(request : HttpResponse,doctor_id : int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctor = doctor)
    except:
        return render(request , "clinic/not_found.html")

    return render(request, "clinic/detail_doctor.html", {"doctor" : doctor, "appointments" : appointments})




def add_appointment(request : HttpResponse ,doctor_id : int):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == "POST":
        appointment = Appointment(doctor=doctor, patient_name = request.POST["patient_name"],
         case_description=request.POST["case_description"],patient_age = request.POST["patient_age"],
         appointment_datetime = request.POST["appointment_datetime"], is_attended = request.POST["is_attended"])
        appointment.save()
        return redirect("clinic:home")

    return render(request ,"clinic/add_appointment.html",{"doctor":doctor})



def appointment_check(request : HttpResponse):
    return render(request,"clinic/appointment_check.html")


def not_found(request : HttpResponse):
    return render(request,"clinic/not_found.html")