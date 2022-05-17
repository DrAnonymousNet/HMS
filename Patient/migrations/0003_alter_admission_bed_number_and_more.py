# Generated by Django 4.0.4 on 2022-05-14 20:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0002_alter_department_about_alter_department_name'),
        ('Patient', '0002_alter_entry_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='bed_number',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Department.bed'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='date_of_discharged',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admission',
            name='discharge_summary',
            field=models.TextField(blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='admission',
            name='reason',
            field=models.TextField(blank=True, max_length=160),
        ),
    ]