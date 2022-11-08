from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length = 2048)
    description = models.TextField()
    rating = models.FloatField()
    experience_years = models.IntegerField(100 )
    specialization_choices = models.TextChoices("specialization", ["surgery" , "familyMedicine" , "dental" , "Audiology" , "Orthopedics & Rheumatology" , "Physiotherapy" , "Cardiac "])
    specialization = models.CharField(max_length = 64 , choices = specialization_choices.choices)

    def __str__(self) -> str:
        return f"{self.name}, {self.description}"


class Appointment(models.Model):
    relation = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    patient_name = models.CharField(max_length = 2048)
    case_description = models.TextField()
    patient_age = models.IntegerField(4)
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.patient_name}, {self.patient_age}"