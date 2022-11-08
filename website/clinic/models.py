from django.db import models

# Create your models here.
class Doctor(models.Model):

    specialization_choices = models.TextChoices("Specialization", ["General Medicine", "heart and blood vessels","Ophthalmology "])

    name = models.CharField(max_length=125)
    description = models.TextField()
    experience_years = models.IntegerField()
    rating = models.FloatField()
    spcialization = models.CharField(max_length=64, choices=specialization_choices.choices)
    

class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)

    patient_name = models.CharField(max_length=125)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField()