# Generated by Django 4.1.3 on 2022-11-06 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('experience_years', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=256)),
                ('case_description', models.TextField()),
                ('patient_age', models.IntegerField()),
                ('appointment_datetime', models.DateTimeField()),
                ('is_attended', models.BooleanField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClinicApp.doctor')),
            ],
        ),
    ]
