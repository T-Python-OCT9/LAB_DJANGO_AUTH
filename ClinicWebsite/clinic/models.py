from django.db import models

# Create your models here.

class Doctor(models.Model):
    class DoctorSpec(models.TextChoices):

        general_doc = 'GD', 'General Doctor'
        dentist = 'DE', 'Dentist'
        psychiatrist = 'PD', 'Psychiatric Doctor'

        
    name = models.CharField(max_length = 256)
    description = models.TextField()
    specialization = models.CharField(max_length = 2, choices = DoctorSpec.choices,
                                        default = DoctorSpec.general_doc)
    experience_years = models.IntegerField()
    rating = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name}, {self.specialization}"

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.PROTECT)

    patient_name = models.CharField(max_length = 256)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateField()
    is_attended = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.patient_name}, {self.appointment_datetime}"