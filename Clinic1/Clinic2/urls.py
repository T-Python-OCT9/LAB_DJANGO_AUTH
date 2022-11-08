from django.urls import path
from . import views

app_name = "Clinic2"

urlpatterns = [
    path("Home/", views.Home, name="Home"),
    path("det/", views.detail, name="detail"),
   
    path("reg/", views.register, name="register"),
      path("in/", views.login, name="login"),
    path("out/", views.logout, name="logout")
   
]