# Generated by Django 4.1.3 on 2022-11-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/images/default.jpg', upload_to='images/'),
            preserve_default=False,
        ),
    ]
