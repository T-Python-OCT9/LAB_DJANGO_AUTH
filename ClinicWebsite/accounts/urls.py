from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.registerPage, name='register_user'),
    path('login/', views.loginPage, name='login_user'),
    path('logout/', views.logoutPage, name='logout_user')
]