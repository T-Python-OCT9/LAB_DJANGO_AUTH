from django.urls import path
from . import views

app_name = "clinic"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("add_doctor/", views.add_doctor, name="add_doctor"),
    path("add_appointment/<doctor_id>/", views.add_appointment, name="add_appointment"),
    path("appointment_check/", views.appointment_check, name="appointment_check"),
    path("detail_doctor/<doctor_id>/", views.detail_doctor , name ="detail_doctor"),
    path("not_found/",views.not_found , name="not_found.html"),
]