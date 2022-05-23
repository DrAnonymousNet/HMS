from django.shortcuts import render, redirect,reverse
from Department.models import Department
from django.http import JsonResponse
from Staff.models import Doctor
from Patient.forms import *
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
    appointments = patient.get_appointment_history()
    drug_prescription_list = DrugPrescription.objects.filter(patient_id=patient.id)
    lab_test_list = LabTest.objects.filter(patient_id=patient.id)
    context = {
        "patient": patient,
        "appointments": appointments,
        "labtests": lab_test_list,
        "drugprescriptions": drug_prescription_list
    }
    return render(request, "patient-page.html", context)

def DrugPrescriptionFormView(request, id):
    patient = Patient.objects.get(id=id)
    form = DrugPrescriptionForm()
    if request.method == "POST":
        form = DrugPrescriptionForm(request.POST)
        if form.is_valid():
            form.instance.prescribing_doctor = Doctor.objects.get(profile=request.user)
            form.instance.patient = patient
            form.instance.save()
            return redirect(reverse("patient-page", kwargs = {"id":id}))
    context = {
        "form":form,
        "patient":patient
    }
    return render(request,"drug_prescription_form.html", context )

def LabTestFormView(request, id):
    patient = Patient.objects.get(id=id)
    form = LabTestForm()
    if request.method == "POST":
        form = LabTestForm(request.POST)
        if form.is_valid():
            form.instance.prescribing_doctor = Doctor.objects.get(profile=request.user)
            form.instance.patient = patient
            form.instance.save()
            return redirect(reverse("patient-page", kwargs = {"id":id}))
    context = {
        "form":form,
        "patient":patient
    }
    return render(request,"lab_test_form.html", context )

def EntryFormView(request, id):
    form = EntryForm()
    patient = Patient.objects.get(id=id)

    context = {
        "form":form,
        "patient":patient

    }
    return render(request, "entryform.html", context)

def AppointmentFormView(request,id):
    form = AppointmentForm()
    patient = Patient.objects.get(id = id)
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.save()
            return redirect(patient.get_absolute_url())

    context = {
        "form":form,
        "patient":patient,
    }
    return render(request, "appointment-form.html", context)

def PatientPrescriptioListView(request, id):
    patient = Patient.objects.get(id=id)
    appointments = patient.get_appointments_history()
    drug_prescription_list = DrugPrescription.objects.filter(patient_id = patient.id)
    lab_test_list = LabTest.objects.filter(patient_id = patient.id)
    context = {
        "patient":patient,
        "appointments":appointments,
        "labtests":lab_test_list,
        "drugprescriptions":drug_prescription_list
    }
    return render(request, "all_prescription_list.html", context)