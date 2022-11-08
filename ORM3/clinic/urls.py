from django.urls import path
from . import views

app_name = "clinic"

urlpatterns = [
    path("doctor/add/", views.add_doctor, name="add_doctor"),
    path("doctor/view/", views.list_doctors, name = "list_doctors"),
    
]