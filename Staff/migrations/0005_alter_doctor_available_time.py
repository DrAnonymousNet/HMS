# Generated by Django 4.0.4 on 2022-05-16 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0004_alter_doctor_subordinate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='available_time',
            field=models.TimeField(blank=True),
        ),
    ]
