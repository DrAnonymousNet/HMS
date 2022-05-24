import datetime

from django.db import models
from Staff.models.staff import *
from Department.models.inventory import *
from Department.models.department import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import gettext as _
from tinymce import HTMLField
from django.db.models import Q
from django.shortcuts import reverse


class Patient(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    department = models.ManyToManyField(Department,blank=True)
    home_address = models.CharField(max_length=50, blank=True)
    next_of_kin_name = models.CharField(max_length=20, blank=True)
    next_of_kin_contact = models.CharField(max_length=20, blank=True)
    admitted = models.BooleanField(default=False)

    #def clean(self):
        #if self.admitted:
         #   admission = Admission.objects.get(for_patient = self, date_of_discharge__isnull = True)

    def __str__(self):
        return self.get_full_name()
    def get_absolute_url(self):
        return reverse("patient-page", kwargs = {"id":self.id})

    def get_admission_history(self):
        return self.admission_set.all()

    def get_full_name(self):
        return f"{self.profile.first_name}"

    def get_medical_log_entries(self):
        return self.entry_set.all()

    def get_present_admission(self):
        return self.admission_set.get(admission_status="Active")
    def get_appointment_history(self):
        return self.appointment_set.all()



class Admission(models.Model):
    status = [
        ("Active", "Active"),
        ("Discharge", "Discharged")
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.OneToOneField(Bed, on_delete=models.CASCADE, blank=True, null=True,
                                      limit_choices_to=Q(status=1))
    reason = models.TextField(max_length=160, blank=True)
    discharge_summary = models.TextField(max_length=160, blank=True)
    date_of_admission = models.DateField(auto_now_add=True)
    date_of_discharged = models.DateField(blank=True, null=True)
    admission_status = models.CharField(choices=status, max_length=10)

    class Meta:
        unique_together = ["patient", "date_of_admission"]

    def clean(self):
        if self.admission_status == 'Admitted':
            self.bed_number.status = 'Occupied'
            self.patient.admitted = True
        if self.admission_status == 'Discharged':
            self.bed_number.status = 'Free'
            self.bed_number = None
            self.date_of_discharged = datetime.datetime.now()
            self.patient.admitted = False

    def __str__(self):
        return f"{self.date_of_admission}" + " "+ str(self.patient)


class Entry(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    content = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    appointment = models.ForeignKey("Appointment", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.content

class LabTestObject(models.Model):
    test_name = models.CharField(max_length=20)
    description = models.TextField(max_length=160)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    price = models.FloatField()

    def __str__(self):
        return f"{self.test_name}"


class LabTest(models.Model):

    urgency_choice = [
        ("Very very Urgent", "Class A"),
        ("Very Urgent", "Class B"),
        ("Not Urgent", "Class C")
    ]

    test = models.ForeignKey(LabTestObject, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    prescribing_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    urgency = models.CharField(choices=urgency_choice, max_length=30)
    appointment= models.ForeignKey("Appointment", on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient} {self.test} {self.date.date()}"


class TestResult(models.Model):
    for_which_test = models.OneToOneField(LabTest, on_delete=models.CASCADE)
    result = models.FileField()
    date = models.DateTimeField(auto_now_add=True)
    lab_attendant = models.ForeignKey(LabAttendance, models.DO_NOTHING)

    def __str__(self):
        return f"{self.for_which_test} Result"


class DrugPrescription(models.Model):
    drug_name = models.CharField(max_length=20)
    dosage_description = models.TextField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.Model)
    prescribing_doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)
    appointment = models.ForeignKey("Appointment", models.CASCADE)

    def __str__(self):
        return self.drug_name


class Appointment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    phone_number = models.CharField(blank=True, max_length=20)
    message = models.TextField(max_length=160 , blank=True)


    def __str__(self):
        return str(self.patient) + str(self.date)

    def clean(self):
        if self.time > datetime.time(14):
            raise ValidationError("Make appointment with a doctor in the morning only")
        if self.doctor.duty_shift != "Morning":
            raise ValidationError("Select A Doctor in the morning duty !")

