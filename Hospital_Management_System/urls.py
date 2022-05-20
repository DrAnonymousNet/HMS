"""Hospital_Management_System URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from .views import index
from Staff.views import doctors_view, doctor_view
from account.views import login_view, logout_view
from Patient.views import appointment_view, confirmation_view, patient_page
from Department.views import departments_view, department_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name = "index"),
    path("staff/", include("Staff.urls")),
    path("login/", login_view, name = "login"),
    path("logout/", logout_view, name="logout"),
    path("appointment/", appointment_view, name="appointment"),
    path("confirmation/", confirmation_view, name = "confirmation"),
    path("doctors/", doctors_view, name = "doctors"),
    path("doctors/<int:id>/", doctor_view, name= "doctor"),
    path("departments/", departments_view, name="departments"),
    path("departments/<int:id>", department_view, name= "department"),
    path("patient/<int:id>", patient_page, name="patient-page" )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_ROOT, document_root = settings.MEDIA_ROOT)


