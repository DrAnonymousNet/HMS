"""Hospital_Management_System URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from .views import index
from account.views import login_view, logout_view
from Patient.views import appointment_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name = "index"),
    path("staff/", include("Staff.urls")),
    path("login/", login_view, name = "login"),
    path("logout/", logout_view, name="logout"),
    path("appointment/", appointment_view, name="appointment")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_ROOT, document_root = settings.MEDIA_ROOT)


