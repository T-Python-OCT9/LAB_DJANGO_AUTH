from django.db import models

# Create your models here.

class doctor(models.Model):
  # specialization_choice=models.TextField("specialization",["Ophthalmology","Pediatrics"] )
   
   name = models.CharField(max_length=1024)
   description = models.TextField()
   experience_years = models.CharField(max_length=1024)
   rating = models.CharField(max_length=1024)
   image = models.ImageField(upload_to="images/")
   #specialization = models.CharField(max_length=64, choices = specialization_choice.choices)
        


class appointment(models.Model):
    doctor = models.ForeignKey(doctor, on_delete = models.CASCADE) 
    patient_name = models.CharField(max_length=1024)
    case_description =  models.TextField()
    patient_age = models.TextField()
    appointment_datetime =models.DateField()
    is_attended = models.BooleanField()