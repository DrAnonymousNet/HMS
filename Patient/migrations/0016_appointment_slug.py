# Generated by Django 4.0.4 on 2022-05-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0015_alter_appointment_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='slug',
            field=models.SlugField(default='12-12-11'),
        ),
    ]
