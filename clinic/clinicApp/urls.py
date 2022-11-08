from django.urls import path
from . import views

app_name = "clinicApp"

urlpatterns = [
    path("doctor/", views.add_doctor, name="add_doctor"),
    path("home/", views.list, name="list_doctors"),
    path("doctor_detail/<doctor_id>", views.doctor_detail, name="doctor_detail"),
 
 

]