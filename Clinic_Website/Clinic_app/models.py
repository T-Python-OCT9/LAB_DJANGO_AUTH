from django.db import models

# Create your models here.


class Doctor(models.Model):
    FIELDS = (
        ('Dentistry', 'Dentistry'),
        ('Pediatrice', 'Pediatrice'),
        ('Dermatology', 'Dermatology'),
        ('General Practitoner', 'General Practitoner'),


    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    specialization = models.CharField(
        max_length=250, choices=FIELDS, default=000)
    experience_years = models.IntegerField()
    rating = models.FloatField()
    


class Appointment(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField(auto_now_add=False)
    is_attended = models.BooleanField()
