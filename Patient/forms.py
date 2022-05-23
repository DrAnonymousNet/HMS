from django import forms
from .models.patient import LabTest,Appointment, Entry,\
    Patient,DrugPrescription,Admission,TestResult, LabTestObject
from Department.models import Department
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = "__all__"

class DrugPrescriptionForm(forms.ModelForm):
    class Meta:
        model = DrugPrescription
        exclude = ["patient", "prescribing_doctor"]

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
        exclude= ["patient", "prescribing_doctor"]

class LabTestObjectForm(forms.ModelForm):
    class Meta:
        model = LabTestObject
        fields = "__all__"

class EntryForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEWidget(attrs={
        'required': True, 'cols': 30, 'rows': 10}
    ))
    class Meta:
        model = Entry
        fields = ["doctor", "date","department", "content"]


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





