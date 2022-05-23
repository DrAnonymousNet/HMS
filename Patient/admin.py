from django.contrib import admin
from .models.patient import *

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(DrugPrescription)
admin.site.register(Admission)
admin.site.register(LabTest)
admin.site.register(TestResult)
admin.site.register(Entry)
admin.site.register(LabTestObject)