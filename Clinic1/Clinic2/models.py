from django.db import models

# Create your models here.


class Doctor(models.Model):
    name  = models.CharField(max_length=2048)
    description  = models.TextField()
    specialization = models.CharField(max_length=2048)
    experience_years = models.TextField()
    rating = models.FloatField()


class Appointment(models.Model):

    Relation = models.ForeignKey(Doctor, on_delete = models.CASCADE )

    patient_name  = models.CharField(max_length=2048)
    case_description  = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField()  