from django.db import models

# Create your models here.

class Doctor(model.model):    
    name = models.CharField(max_length = 256)
    description = models.TextField()
    specialization = models.CharField(max_length = 2, choices = DoctorSpec.choices,default = DoctorSpec.general_doc)
    experience_years = models.IntegerField()
    rating = models.FloatField()

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.PROTECT)
    patient_name = models.CharField(max_length = 256)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateField()
    is_attended = models.BooleanField()

    
    
### Models

- Doctor model should have
- - name
- - description
- - specialization (use text choices)
- - experience_years
- - rating



- Appointment Model
- - Relation with doctor
- - patient_name
- - case_description
- - patient_age
- - appointment_datetime
- - is_attended
