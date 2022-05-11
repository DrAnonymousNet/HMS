from django.db import models
from datetime import time, timedelta
from Department.models.department import Department
from django.contrib.auth.models import User

shift_choice = [
    ("Morning", "Morning"),
    ("Afternoon", "Afternoon"),
    ("Night", "Night")
]

class Staff(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.ForeignKey("Qualification", on_delete=models.CASCADE)
    about = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey("Department", on_delete=models.DO_NOTHING),
    duty_shift = models.CharField(choices=shift_choice, max_length= 20)

    class Meta:
        abstract = True

class Doctor(Staff):
    available_time = models.TimeField()


class Nurse(Staff):
    pass

class LabAttendance(Staff):
    pass


class Qualification(models.Model):
    qualification = models.CharField( max_length= 20)
    school = models.CharField(max_length=20)
    start_year = models.DateField()
    end_year = models.DateField()





