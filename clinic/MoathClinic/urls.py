from django.urls import path
from . import views

app_name = "Clincapp"

urlpatterns = [
    path("home/", views.Home_Page,name="homepage"),
    path('galleyr/',views.Gallery , name="gallery"),
    path("list/", views.list_doctors, name="list_doctors"),
    path('add/doctors/',views.add_Doctors,name="add_doctors"),
    path("doctor/detail/<doctor_id>/", views.doctor_detail, name="doctor_detail"),
    path("doctor/update/<doctor_id>/", views.update_doctor, name="update_doctor"),
    path("doctor/delete/<doctor_id>/", views.delete_doctor, name="delete_doctor"),
    path("doctor/<doctor_id>/appointment/new/", views.add_appointment, name="add_appointment"),
]
