from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 256)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    spec_choices = models.TextChoices('specialization' , 'FamilyMedicine Surgery Anesthesiology Physiotherapy Dental' )
    SPECIALIZATION_CHOICES = [
        ("FAMILYMEDICINE", 'Family medicine'),
        ("SURGERY", 'Surgery'),
        ("ANESTHESIOLOGY", 'Anesthesiology'),
        ("PHSIOTHERAPY",'Physiotherapy'),
        ("DENTAL",'Dental')
    ]
    specialization = models.CharField(
        max_length=256,
        choices= spec_choices.choices,
        default=SPECIALIZATION_CHOICES[0][0],
    )
    experience_years = models.IntegerField()
    rating = models.FloatField()

    # for admin page to be readed easily
    def __str__(self) -> str:
        return f"{self.name}"

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=256)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended =models.BooleanField()

    def __str__(self):
        return f"{self.patient_name}, {self.case_description}"