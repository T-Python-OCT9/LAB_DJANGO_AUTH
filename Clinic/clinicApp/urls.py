from django.urls import path
from.import views


app_name="clinicApp"

urlpatterns = [

    path("home/",views.home,name="home"),
    path("doctor/",views.addDoctor,name="doctor"),
    path("do",views.postDoctor,name="po"),
    path("view/<doctor_id>",views.view_info,name="views"),
    path("post/<doctor_id>/appointment/new/",views.addAppointment,name="info")
  
]