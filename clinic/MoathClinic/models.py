from django.db import models

# Create your models here.

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    specialization = models.TextField()
    experience_years = models.CharField(max_length=64)
    rating = models.FloatField()



class Appointment(models.Model): 
    appointment = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    Patient_Name = models.CharField(max_length=256)
    Patient_Age = models.IntegerField()
    Relation_With_Doctor = models.CharField(max_length=256)
    Case_Description = models.TextField()
    Appointment_Datetime = models.DateTimeField()
    Is_Attended=models.BooleanField()

