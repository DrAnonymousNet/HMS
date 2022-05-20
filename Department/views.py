from django.shortcuts import render
from .models import Department
# Create your views here.

def departments_view(request):
    departments = Department.objects.all()

    context = {
        "departments":departments
    }
    return render(request, "department.html", context)

def department_view(request, id):
    department = Department.objects.get(id=id)
    context = {
        "department":department
    }
    return render(request,"department-single.html", context)