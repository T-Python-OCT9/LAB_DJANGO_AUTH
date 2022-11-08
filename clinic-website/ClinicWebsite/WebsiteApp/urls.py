from django.urls import path
from . import views

app_name = "WebsiteApp"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("gallary/",views.gallary,name="gallary"),
    path("add_doctor/",views.add_doctor,name="add_doctor"),
    path("view/",views.doctor_list,name="doctor_list"),
    path("detail/<doctor_id>/",views.doctor_detail,name="doctor_detail"),
    path("book",views.view_appointment, name="view_appointment"),
    path("appointments/<doctor_id>", views.doctor_appointments,name="doctor_appointments"),

]