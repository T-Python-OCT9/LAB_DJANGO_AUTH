from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    char_specialization=models.TextChoices("specialization type" ,["Family medicine" ,"surgery" , "Dental"])
    specialization=models.CharField(max_length=64 , choices =char_specialization.choices)
    experience_years = models.IntegerField()
    rating = models.FloatField()
    


class Appointment(models.Model): 
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    Patient_Name = models.CharField(max_length=256)
    Patient_Age = models.IntegerField()
    Relation_With_Doctor = models.CharField(max_length=256)
    Case_Description = models.TextField()
    Appointment_Datetime = models.DateTimeField()
    Is_Attended=models.BooleanField()