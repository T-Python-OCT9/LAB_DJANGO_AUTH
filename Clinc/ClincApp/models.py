from django.db import models

# Create your models here.
class Doctor(models.Model):

    spe=[
        ("O","orthodontics"),
        ("F","fillings"),]
    name=models.CharField(max_length=300)
    description=models.TextField()
    specialization=models.CharField(max_length=200, choices=spe , default="O")
    experience_years=models.IntegerField()
    rating=models.FloatField()


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    patient_name=models.CharField(max_length=300)
    case_description=models.TextField()
    patient_age=models.IntegerField()
    appointment_datetime=models.DateTimeField()
    is_attended=models.BooleanField()




