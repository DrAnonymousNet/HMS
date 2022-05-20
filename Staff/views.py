from django.shortcuts import render, get_object_or_404
from .models.staff import Doctor, LabAttendance, Qualification
from Department.models import Department


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

def doctors_view(request):
    doctors = Doctor.objects.all()
    departments = Department.objects.all()
    context = {
        "doctors":doctors,
        "departments":departments
    }
    return render(request, "doctor.html", context)

def doctor_view(request, id):
    doctor = get_object_or_404(Doctor, id = id)
    qualifications = Qualification.objects.filter(for_who = doctor.profile)
    context = {
        "doctor":doctor,
        "qualifications":qualifications
    }
    return render(request, "doctor-single.html", context)

