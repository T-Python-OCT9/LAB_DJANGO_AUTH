from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor,Appointments

# Create your views here.
def home(request : HttpRequest):
    
    return render(request, "WebsiteApp/index.html")



def gallary(request : HttpRequest):
    
    return render(request, "WebsiteApp/gallary.html")



def add_doctor(request : HttpRequest):
    if request.method == "POST":
        new_doc = Doctor(Docname=request.POST["Docname"], DocDescrip = request.POST["DocDescrip"], DocRate=request.POST["Doctor_Rate"], experience_years = request.POST["experience_years"],DocSpecialization=request.POST["DocSpecialization"])
        new_doc.save()
    
    return render(request, "WebsiteApp/add_doctor.html",{"Doctor" : Doctor})


def doctor_list(request :HttpRequest):
    if "search" in request.GET:
        doctors = Doctor.objects.filter(Docname__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()
        return render(request, "WebsiteApp/doctor_list.html", {"doctors" : doctors})
        

def doctor_detail(request : HttpRequest, doctor_id : int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request , "WebsiteApp/notFound.html")

    return render(request, "WebsiteApp/doctor_detail.html", {"doctor" : doctor})



def doctor_appointments(request :HttpRequest,doctor_id:int):
    try:
        Doctor=Doctor.objects.get(id=doctor_id)
        appointment = Appointments.objects.filter(Doctor=Doctor ) 
    except:
        return render(request , "WebsiteApp/notFound.html")
    return render(request,"WebsiteApp/doctor_appointments.html",{"Doctor":Doctor},{"appointment":appointment})

   
def view_appointment(request :HttpRequest):
    doctors = Doctor.objects.all()
        
    if request.method == "POST":
        doctor=Doctor.objects.get(id=request.POST["doctor_id"])
        new_appointment = Appointments(Doctor =doctor,p_name=request.POST["p_name"], case_description = request.POST["case_description"], p_age=request.POST["p_age"], Appointment_datetime = request.POST["Appointment_datetime"],is_attend=request.POST["is_attend"])
        new_appointment.save()
        new_appointment.Appointment_datetime = new_appointment.Appointment_datetime.isoformat("T", "hours").replace("+", ":")
        return redirect("WebsiteApp:doctor_appointments",doctor.id)
       
    return render(request, "WebsiteApp/book_appointment.html", {"doctors" : doctors})




