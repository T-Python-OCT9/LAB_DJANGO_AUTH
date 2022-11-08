from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Doctor, Appointment
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

# Create your views here.
def homePage(request: HttpRequest):
    doctors = Doctor.objects.all()[:4]
    if request.user.has_perm('clinic.delete_appointment'):
        group = 'admin'
    else:
        group = 'user'
    context = {'doctors':doctors, 'group':group}
    return render(request, 'clinic/home.html', context)

@login_required()
def getDoctors(request: HttpRequest):
    doctors = Doctor.objects.all()
    if request.user.has_perm('clinic.delete_appointment'):
        group = 'admin'
    else:
        group = 'user'
    for doctor in doctors:
        doctor.appointments = Appointment.objects.filter(doctor=doctor).count
    context = {'doctors':doctors, 'group':group}
    return render(request, 'clinic/list.html', context)

@login_required()
def addDoctor(request: HttpRequest):
    doctor_specializations = Doctor.specialization_choices.choices
    if request.user.has_perm('clinic.delete_appointment'):
        group = 'admin'
    else:
        group = 'user'
    if request.method == 'POST':
        doctor = Doctor(name=request.POST['name'], description=request.POST['description'], experience_years=request.POST['experience_years'], rating=request.POST['rating'], specialization=request.POST['specialization'], image=request.FILES['image'])
        doctor.save()
        return redirect('clinic:doctors')
    context = {'doctor_specializations':doctor_specializations, 'group':group}
    return render(request, 'clinic/add.html', context)

@login_required()
def updateDoctor(request: HttpRequest, doctor_id: int):
    if request.user.has_perm('clinic.delete_appointment'):
        group = 'admin'
    else:
        group = 'user'
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        doctor_specializations = Doctor.specialization_choices.choices
        if request.method == 'POST':
            doctor.name = request.POST['name']
            doctor.description = request.POST['description']
            doctor.experience_years = request.POST['experience_years']
            doctor.rating = request.POST['rating']
            doctor.specialization = request.POST['specialization']
            if request.FILES:
                doctor.image = request.FILES['image']
            doctor.save()
            return redirect('clinic:doctors')
    except:
        return render(request, 'clinic/not_found.html')
    context = {'doctor_specializations':doctor_specializations, 'doctor':doctor, 'group':group}
    return render(request, 'clinic/update.html', context)

@login_required()
def removeDoctor(request: HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        doctor.delete()
        return redirect('clinic:doctors')
    except:
        return render(request, 'clinic/not_found.html')

@login_required()
def doctorDetail(request: HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        if request.user.has_perm('clinic.delete_appointment'):
            appointments = Appointment.objects.filter(doctor=doctor)
            group = 'admin'
        else:
            appointments = Appointment.objects.filter(doctor=doctor, name=request.user.username)
            group = 'user'
        count = appointments.count
        date = datetime.isoformat(datetime.today(), timespec='minutes').replace('+',':')
    except:
        return render(request, 'clinic/not_found.html')
    context = {'doctor':doctor, 'appointments':appointments, 'count':count, 'date':date, 'group':group}
    return render(request, 'clinic/detail.html', context)

@login_required()
def bookAppointment(request: HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        if request.method == 'POST':
            print(request.POST)
            new_appointment = Appointment(doctor=doctor, name=request.POST['name'], case=request.POST['case'], age=request.POST['age'], date=request.POST['date'].replace(':','+'))
            new_appointment.save()
    except:
        return render(request, 'clinic/not_found.html')
    return redirect('clinic:detail', doctor.id)

def searchDoctor(request: HttpRequest):
    if request.user.has_perm('clinic.delete_appointment'):
        group = 'admin'
    else:
        group = 'user'
    doctors = Doctor.objects.all().filter(name__contains=request.GET.get('doctor', ''))
    context = {'doctors':doctors, 'group':group}
    return render(request, 'clinic/search.html', context)

def galleryPage(request: HttpRequest):
    if request.user.has_perm('clinic.delete_appointment'):
        group = 'admin'
    else:
        group = 'user'
    context = {'group':group}
    return render(request, 'clinic/gallery.html', context)

