import datetime

from django.db import models
from datetime import time, timedelta

from django.contrib.auth.models import User
from Department.models.department import *

shift_choice = [
    ("Morning", "Morning"),
    ("Afternoon", "Afternoon"),
    ("Night", "Night")
]

class Staff(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15)
    duty_shift = models.CharField(choices=shift_choice, max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE , default=1)
    profile_picture = models.ImageField(upload_to='profile_picture', blank=True)
    facebook = models.URLField(blank=True)
    linkedln = models.URLField(blank= True)
    twitter = models.URLField(blank=True)
    class Meta:
        abstract = True


class Doctor(Staff):
    qualification = models.OneToOneField("Qualification", on_delete=models.CASCADE)
    available_time = models.TimeField(blank=True)
    subordinate = models.ForeignKey('Doctor', on_delete=models.CASCADE, blank= True, null=True)

    def clean(self):
        if self.duty_shift == "Morning":
            self.available_time = datetime.time(hour = 13)
        elif self.duty_shift == "Afternoon":
            self.available_time = datetime.time(20)

    def get_fullname(self):
        return f"{self.profile.first_name} {self.profile.last_name}"


    def __str__(self):
        return "Dr " + str(self.get_fullname())
class Nurse(Staff):
    pass


class LabAttendance(Staff):

    def __str__(self):
        return self.profile.first_name


class Qualification(models.Model):
    for_who = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=20)
    school = models.CharField(max_length=20)
    start_year = models.DateField()
    end_year = models.DateField()
    more_info = models.TextField(blank=True)

    class Meta:
        ordering = ["start_year"]
    def __str__(self):
        return f"{self.qualification}  {self.for_who}"
