from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Doctor(models.Model):

    specialization_choices = models.TextChoices("specialization_choices", ["Ear", "Nose", "Thraut"])

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    specialization = models.CharField(max_length=64, choices = specialization_choices.choices, default=specialization_choices.Nose)
    experience_years = models.CharField(max_length=64)
    rating = models.FloatField()


class Appointment(models.Model): 
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    pationt_name = models.CharField(max_length=64)
    case_description = models.TextField()
    patient_age = models.DateTimeField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField()

