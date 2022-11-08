from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('register/' , views.register , name= "register"),
    path('login/' , views.logIn , name='logIn'),
    path('logout/' , views.logOut , name='logOut')
]