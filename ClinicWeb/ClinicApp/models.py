from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''

Models

* Doctor model should have
- name
- description
- specialization (use text choices)
- experience_years
- rating

* Appointment Model
- Relation with doctor
- patient_name
- case_description
- patient_age
- appointment_datetime
- is_attended

'''


class Doctor(models.Model):
    name = models.CharField(max_length = 256)
    description = models.TextField()
    spec_choices = models.TextChoices('specialization' , 'Pediatriciane Dentist Ophthalmologist' )
    SPECIALIZATION_CHOICES = [
        ("Pediatriciane"),
        ("Dentist")
        ("Ophthalmologist")
    ]
    specialization = models.CharField(
        max_length=256,
        choices= spec_choices.choices,
        default=SPECIALIZATION_CHOICES[0][0],
    )
    experience_years = models.IntegerField()
    rating = models.FloatField()


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=256)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended =models.BooleanField()


def __str__(self):
        return f"{self.patient_name}, {self.case_description}"

