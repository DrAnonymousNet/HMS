from django.contrib import admin
from .models.staff import *



# Register your models here.
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Qualification)
admin.site.register(LabAttendance)