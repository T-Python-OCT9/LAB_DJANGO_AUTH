from django.shortcuts import render ,redirect
from django.http import HttpRequest 
from .models import Doctor ,Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request:HttpRequest):

    return render(request, 'ClinicApp/base.html')

def add_Doctors(request:HttpRequest):
    if request.method == "POST":
        new_Doctors = Doctor (name=request.POST["name"], description = request.POST["description"], specialization=request.POST["specialization"], experience_years = request.POST["experience_years"],rating=request.POST["rating"])
        new_Doctors.save()

    return render(request,"ClinicApp/add_doctors.html")
    

def doctors(request:HttpRequest):

    if "search" in request.GET:
        doctors = Doctor.objects.filter(name__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()

    return render(request, "ClinicApp/list_doctors.html", {"doctors" : doctors})

def view_doctor(request:HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctor = doctor)
    except:
        return render(request, "ClinicApp/not_found.html")

    context = {'doctor': doctor, 'appointments': appointments}
    return render(request, "ClinicApp/view_doctor.html", context)

def appointment(request:HttpRequest, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, "ClinicApp/appointment.html",{'doctor': doctor})

def add_appointment(request:HttpRequest, doctor_id: int):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == "POST":
        new_appointment = Appointment(doctor=doctor,pationt_name=request.POST.get('pationt_name'), case_description= request.POST.get('case_description'),patient_age = request.POST.get('patient_age') ,appointment_datetime= request.POST.get('appointment_datetime'),is_attended= request.POST.get('is_attended'))
        new_appointment.save()
    
    return redirect(request,"ClinicApp:view_doctor")#pro<<


def update_doctor(request: HttpRequest, doctor_id:int):
    pass


 #--------
def register_user(request : HttpRequest):

    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()

    return render(request, "ClinicApp/register.html")


def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        if user:
            login(request, user)
            return redirect("ClinicApp:list_posts")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "ClinicApp/login.html", {"msg" : msg})


def logout_user(request: HttpRequest):

    logout(request)

    return redirect("ClinicApp:view_doctor")

       