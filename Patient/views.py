from django.shortcuts import render
from Department.models import Department
from django.http import JsonResponse
from Staff.models import Doctor
from Patient.forms import AppointmentForm2
from Patient.models import *
from django.core.serializers import serialize
from .models import *
import json


# Create your views here.


def appointment_view(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if is_ajax:
        if request.method == "POST":
            data = json.load(request)
            dept = data.get("payload")
            doctor = Doctor.objects.filter(department__name=dept["dept"])
            doclist = {}
            for i, data in enumerate(doctor):
                doclist[i] = data.profile.first_name
            doclist["len"] = doctor.count()
            # print(serialize(queryset=doctor, format="json"))

            return JsonResponse(doclist)
    if request.method == "POST":
        doctor = request.POST.get("doctor")
        doc = doctor[doctor.index("Dr")+3:]

        Appointment.objects.create(
            date = request.POST.get("date"),
            phone_number = request.POST.get("phone"),
            doctor = Doctor.objects.get(profile__first_name = doc),
            time = request.POST.get("time"),
            message = request.POST.get("message"),
            patient = Patient.objects.get_or_create(
                profile__first_name=request.POST.get("name").split(" ")[0])

        )
        #print(request.POST)

    department = Department.objects.all()
    form = AppointmentForm2()

    context = {
        "departments": department,
        "form":form
    }
    return render(request, "appointment.html", context)


def confirmation_view(request):
    return render(request, "confirmation.html")

def patient_page(request, id):
    patient = Patient.objects.get(id=id)
    context = {
        "patient":patient
    }
    return render(request, "patient-page.html", context)
