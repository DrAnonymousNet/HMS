from django.shortcuts import render
from .models.staff import Doctor, LabAttendance

# Create your views here.


def profile(request):
    doctor = Doctor.objects.get(id=2)
    appointments = doctor.appointment_set.all()
    patient = doctor.department.patient_set.all()
    patient_count = patient.count()
    admitted_count = patient.filter(admitted = True).count()

    context = {
        "appointments":appointments,
        "patient_count":patient_count,
        "admitted_count":admitted_count,

    }
    return render(request, "staffprofile.html", context)

#def labAt(request):

