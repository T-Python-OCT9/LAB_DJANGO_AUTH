from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length = 256)
    description = models.TextField()
    spec_choices = models.TextChoices("spec type",["Family medicine","Surgery","Dental"])
    spec = models.CharField(max_length = 64, choices = spec_choices.choices )
    experience_years = models.IntegerField()
    rating = models.FloatField()


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=256)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended =models.BooleanField()

