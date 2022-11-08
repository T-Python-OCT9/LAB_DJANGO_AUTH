from django.db import models

# Create your models here.

class Doctor(models.Model):
   
    doc_spec_choices = models.TextChoices("DocSpecialization", ("Obstetrics/Gynecology","Anesthesiology","Cardiology","Critical Care Medicine","Dermatology","Diagnostic Radiology","Emergency Medicine","Gastroenterology","Family Medicin","Hematology"))
    Docname = models.CharField(max_length=256)
    DocDescrip = models.TextField()
    DocRate = models.FloatField()
    experience_years = models.IntegerField()
    DocSpecialization =models.CharField(max_length=215, choices = doc_spec_choices.choices, default= doc_spec_choices.Anesthesiology)
    
   

class Appointments(models.Model):

    Doctor=models.ForeignKey(Doctor , on_delete=models.CASCADE)
    p_name = models.CharField(max_length=256)
    case_description = models.TextField()
    p_age = models.IntegerField()
    Appointment_datetime = models.DateTimeField(auto_now=True)
    is_attend=models.BooleanField()




