from django.urls import path
from . import views

app_name="ClinicApp"


urlpatterns = [

    path("", views.home, name="home"),
    path("add/doctors/",views.add_Doctors,name="add_doctors"),
    path("doctors/", views.doctors, name="list_doctors"),
    path("view/<int:doctor_id>/", views.view_doctor, name="view_doctor"), 
    path("view/<int:doctor_id>/appointment/", views.appointment, name="appointment"),
    path("add_appointment/<int:doctor_id>/", views.add_appointment, name="add_appointment"),
    
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user")
    
    
    
]
