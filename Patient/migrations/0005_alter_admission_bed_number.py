# Generated by Django 4.0.4 on 2022-05-14 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0002_alter_department_about_alter_department_name'),
        ('Patient', '0004_alter_admission_bed_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='bed_number',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Department.bed'),
        ),
    ]