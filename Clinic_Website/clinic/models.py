from django.db import models

# Create your models here.

class Doctor(models.Model):
    specialization_choices = models.TextChoices("specialization"
    ,["Anesthesiology","Dermatology","Ophthalmology","Pediatrics"])

    name = models.CharField(max_length=512)
    description = models.TextField()
    specialization = models.CharField(max_length=20,choices=specialization_choices.choices)
    experience_years = models.IntegerField()
    rating = models.FloatField()

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    patient_name = models.CharField(max_length=512)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField()