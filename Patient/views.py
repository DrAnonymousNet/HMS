from django.shortcuts import render
from Department.models import Department
from .models import *
# Create your views here.


def appointment_view(request):
    department = Department.objects.all()

    context = {
        "departments":department,
    }
    return render(request, "appointment.html", context)