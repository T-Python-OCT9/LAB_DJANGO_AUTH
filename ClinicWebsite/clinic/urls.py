from django.urls import path
from . import views

app_name = 'clinic'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('doctors/', views.getDoctors, name='doctors'),
    path('doctors/add/', views.addDoctor, name='add'),
    path('doctor/update/<int:doctor_id>/', views.updateDoctor, name='update'),
    path('doctors/remove/<int:doctor_id>/', views.removeDoctor, name='remove'),
    path('doctor/<int:doctor_id>/', views.doctorDetail, name='detail'),
    path('book/doctor/<int:doctor_id>/', views.bookAppointment, name='book'),
    path('search/', views.searchDoctor, name='search'),
    path('gallery/', views.galleryPage, name='gallery')
]