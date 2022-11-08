from django.urls import path
from . import views

app_name = "clinic"

urlpatterns = [
    path('home/' , views.home , name='home'),
    path('doctors/' , views.all_doctors , name='all_doctors'),
    path("add_doctor/" , views.add_new_doctor , name="add_new_doctor"),
    path("list/doctor" , views.list_doctors , name="list_doctors"),
    path("appointment/" , views.appointments , name='appointments'),
    path("detail/<Doctor_id>/" , views.Doctor_detail , name="Doctor_detail"),
    path("sorry/" , views.only_manager , name='only_manager'),
]
