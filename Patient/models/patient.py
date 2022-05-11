from django.db import models
from Staff.models.staff import *
from Department.models.inventory import *
from Department.models.department import *


class Patient(models.Model):
    name = models.CharField( max_length=50)
    DOB = models.DateField()
    phone_number = models.CharField(max_length=15)
    department = models.ManyToManyField(Department, on_delete=models.DO_NOTHING)
    home_address = models.CharField(max_length=50)
    next_of_kin_name = models.CharField(max_length=20)
    next_of_kin_contact = models.CharField(max_length=20)
    admitted = models.BooleanField()



class Admission(models.Model):
    status = [
        ("Active", "Active"),
        ("Discharge", "Discharged")
    ]
    for_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.OneToOneField(Bed, on_delete=models.CASCADE)
    reason = models.CharField(max_length=160)
    discharge_summary = models.CharField(max_length=160)
    date_of_admission = models.DateField()
    date_of_discharged = models.DateField()
    admission_status = models.CharField(choices=status)

    class Meta:
        unique_together = ["patient", "date_of_admission"]


class Entry(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    content = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()


class LabTest(models.Model):
    urgency_choice = [
        ("Very very Urgent", "Class A"),
        ("Very Urgent", "Class B"),
        ("Not Urgent", "Class C")
    ]
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=160)
    prescribing_doctor = models.ForeignKey(Doctor ,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    urgency = models.CharField(choices= urgency_choice)

class TestResult(models.Model):
    for_which_test = models.OneToOneField(LabTest, on_delete=models.CASCADE)
    result = models.FileField()
    date = models.DateTimeField(auto_now_add=True)
    lab_attendant = models.ForeignKey(LabAttendance, models.DO_NOTHING)



class DrugPrescription(models.Model):
    name = models.CharField(max_length=20)
    dosage_description = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.Model)
    prescribing_doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)

    date = models.DateField()



class Appointment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    phone_number = models.CharField(blank=True, max_length=20)
    message = models.CharField(max_length=160)

