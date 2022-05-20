from django import forms
from .models.patient import LabTest,Appointment, Entry,\
    Patient,DrugPrescription,Admission,TestResult
from Department.models import Department


class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = "__all__"

class DrugPrescriptionForm(forms.ModelForm):
    class Meta:
        model = DrugPrescription
        exclude = ["patient", "doctor"]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"


class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = "__all__"

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = "__all__"

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["doctor", "date", "content"]


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = "__all__"

class AppointmentForm2(forms.Form):
    department = forms.ModelChoiceField(Department.objects.all())
    doctor = forms.ChoiceField( required=True)
    date = forms.DateField
    time = forms.TimeField()
    phone = forms.IntegerField()
    message = forms.Textarea()





