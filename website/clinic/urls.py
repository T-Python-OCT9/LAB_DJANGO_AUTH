from django.urls import path
from . import views
app_name= "clinic"
urlpatterns=[
    path("home/", views.home, name="home"),
    path("details/",views.detailPage,name="details"),
    path("book/",views.bookingpage,name="book"),
    path('add/', views.addDoctor, name='add'),
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user")
    
]