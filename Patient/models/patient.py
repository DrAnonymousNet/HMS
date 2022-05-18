import datetime

from django.db import models
from Staff.models.staff import *
from Department.models.inventory import *
from Department.models.department import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import gettext as _


class Patient(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField()
    phone_number = models.CharField(max_length=15)
    department = models.ManyToManyField(Department)
    home_address = models.CharField(max_length=50)
    next_of_kin_name = models.CharField(max_length=20)
    next_of_kin_contact = models.CharField(max_length=20)
    admitted = models.BooleanField()

    #def clean(self):
        #if self.admitted:
         #   admission = Admission.objects.get(for_patient = self, date_of_discharge__isnull = True)

    def __str__(self):
        return self.get_full_name()

    def get_admission_history(self):
        return self.admission_set.all()

    def get_full_name(self):
        return f"{self.profile.first_name}"

    def get_medical_log_entries(self):
        return self.entry_set.all()

    def get_present_admission(self):
        return self.admission_set.get(admission_status="Active")

    def get_admission_history(self):
        return self.admission_set.all()


class Admission(models.Model):
    status = [
        ("Active", "Active"),
        ("Discharge", "Discharged")
    ]
    for_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.OneToOneField(Bed, on_delete=models.CASCADE, blank=True, null=True)
    reason = models.TextField(max_length=160, blank=True)
    discharge_summary = models.TextField(max_length=160, blank=True)
    date_of_admission = models.DateField()
    date_of_discharged = models.DateField(blank=True, null=True)
    admission_status = models.CharField(choices=status, max_length=10)

    class Meta:
        unique_together = ["for_patient", "date_of_admission"]

    def clean(self):
        if self.for_patient.admitted and not self.date_of_discharged:
            raise ValidationError("This Patient is Admitted Already")
        if self.admission_status == "Discharge" and not self.date_of_discharged:
            raise ValidationError("A discharged admission  profile status must have a discharge date")

        if self.admission_status == "Active" and self.date_of_discharged:
            raise ValidationError("An active admission status cannot have a discharge date")
        elif self.admission_status == "Active" and not self.bed_number:
            raise ValidationError("Set the patient's Bed")
        if self.bed_number.status == "Occupied":
            raise ValidationError("Bed is occupied by a patient")


        if self.admission_status == "Discharge":
            self.for_patient.admitted = False
            self.for_patient.save()
            self.bed_number.status = "Free"
            self.bed_number.save()
            self.bed_number = None
        elif self.admission_status == "Active" :
            self.for_patient.admitted = True
            print(self.bed_number.status)
            self.bed_number.status  = "Occupied"
            self.bed_number.save()

    def __str__(self):
        return f"{self.date_of_admission}" + " "+ str(self.for_patient)


class Entry(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    content = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.content

class LabTest(models.Model):
    urgency_choice = [
        ("Very very Urgent", "Class A"),
        ("Very Urgent", "Class B"),
        ("Not Urgent", "Class C")
    ]
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=160)
    prescribing_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    urgency = models.CharField(choices=urgency_choice, max_length=30)

    def __str__(self):
        return f"{self.name} {self.patient} {self.date.date()}"


class TestResult(models.Model):
    for_which_test = models.OneToOneField(LabTest, on_delete=models.CASCADE)
    result = models.FileField()
    date = models.DateTimeField(auto_now_add=True)
    lab_attendant = models.ForeignKey(LabAttendance, models.DO_NOTHING)

    def __str__(self):
        return f"{self.for_which_test} Result"


class DrugPrescription(models.Model):
    name = models.CharField(max_length=20)
    dosage_description = models.TextField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.Model)
    prescribing_doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    phone_number = models.CharField(blank=True, max_length=20)
    message = models.CharField(max_length=160)

    def __str__(self):
        return str(self.patient) + str(self.date)

    def clean(self):
        if self.time > datetime.time(14):
            raise ValidationError("Make appointment with a doctor in the morning only")
        if self.doctor.duty_shift != "Morning":
            raise ValidationError("Select A Doctor in the morning duty !")

