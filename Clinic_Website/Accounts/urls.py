from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views

app_name = "Clinic_app"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/",
         views.logout, name="logout"),
]
