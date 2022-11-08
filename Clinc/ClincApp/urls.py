from django.urls import path
from . import views

app_name = "ClincApp"

urlpatterns = [
path("home/",views.home,name="home"),
path("add/",views.add , name="add"),
path("viwe_details/<d_id>/", views.viwe_details , name="viwe_details"),
path("search/",views.search,name="search"),
path("doctor/<doctor_id>/appointment/new/", views.book_abiontment, name="book_abiontment"),
]
