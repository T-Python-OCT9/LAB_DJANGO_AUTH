# Generated by Django 4.1.3 on 2022-11-11 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(choices=[('Anesthesiology', 'Anesthesiology'), ('Dermatology', 'Dermatology'), ('Ophthalmology', 'Ophthalmology'), ('Pediatrics', 'Pediatrics')], max_length=20),
        ),
    ]
