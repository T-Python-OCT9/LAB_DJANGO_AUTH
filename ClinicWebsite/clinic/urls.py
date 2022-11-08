from django.urls import path
from . import views



app_name = "clinic"


urlpatterns = [

    path("", views.home_page, name="home_page"),
    path("error/", views.error_page , name="error_page"),
    path("list/", views.list_doctors, name="list_doctors"),
    path("details/<doc_id>/", views.detail_page, name="detail_page"),
    path("add/doctor/", views.add_doctor, name="add_doctor"),
    path("<doc_id>/appointment/new/", views.make_appointment, name="make_appointment")


]