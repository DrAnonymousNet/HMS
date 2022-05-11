from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.db.utils import IntegrityError
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission, User
from Staff.models.staff import *
from Patient.models.patient import *
from Department.models.department import *



Doctor_Groups = ["Residents", "Consultant", "Interns", "Registrars"]
Doctor_Permission = [
        "can admit", "can prescribe",
        "can discharge",
        "can book surgery", "can diagnose", "can have intern", 'can read prescription', 'can create testresult',
        "can read test result",
    ]
permissions = {"Consultant": Permission.objects.all(),
     "Interns": Permission.objects.filter(name__contains = "view"),
     "Residents":  Permission.objects.exclude(name__contains = "delete"),
    "Registrars": Permission.objects.all()
     }


class Command(BaseCommand):
    help = 'Add new Permission'
    def handle(self, *args, **options):
        for c in Doctor_Groups:
            try:
             group = Group.objects.get(name = c)
             group.permissions.set(permissions[c])
             group.save()
            except :
                raise CommandError(f' Could not add {permissions[c]} permission in Group {group}')
            self.stdout.write(self.style.SUCCESS(f'New permissions added to group {c} Successfully'))