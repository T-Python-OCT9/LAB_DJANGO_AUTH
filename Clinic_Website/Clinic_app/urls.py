from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views

app_name = "Clinic_app"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/add_doctors", views.add_doctor, name="add_doctor"),
    path("home/updeat_doctors/<doctor_id>",
         views.update_doctor, name="update_doctor"),
    path("home/detail/<doctor_id>", views.detail_doctor, name="detail_doctor"),
    path("home/delete/<doctor_id>", views.delete_doctor, name="delete_doctor"),
    path("home/doctors/<doctor_id>/add_appointment/new",
         views.add_appointment, name="add_appointment")

]
