from django.db import models

# Create your models here.



class Doctor(models.Model):
    spe=[
        ("O","orthodontics"),
        ("F","fillings"),
        ("Or","oral medicine")
    ]
    name=models.CharField(max_length=256)
    description=models.TextField()
    specialization=models.CharField(max_length=256, choices=spe, default="O")
    experience_years=models.CharField(max_length=256)
    rating=models.FloatField()

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=256)
    case_description=models.TextField()
    patient_age=models.CharField(max_length=256)
    appointment_datetime=models.DateTimeField()
    is_attended=models.BooleanField()
# Create your models here.