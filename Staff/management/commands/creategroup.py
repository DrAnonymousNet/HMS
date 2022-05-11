from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.db.utils import IntegrityError
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission, User
from Staff.models.staff import *
from Patient.models.patient import *
from Department.models.department import *



Doctor_Groups = ["Residents", "Consultant", "Interns", "Registrars"]


class Command(BaseCommand):
    help = 'Add new Groups'
    def add_arguments(self, parser):
        parser.add_argument('name', nargs= '?', type=str)
    def handle(self, *args, **options):
        c = options['name']
        if options['name']:
            try:
                group = Group.objects.create(name=options['name'])
                group.save()
            except:
                raise CommandError(f'{c} already in Group List')
            self.stdout.write(self.style.SUCCESS(f'New Group {c} Successfully'))
        else:
            for c in Doctor_Groups:
                try:
                    group = Group.objects.create(name = c)
                    group.save()
                except :
                    raise CommandError(f'{c} already in Group List')
                self.stdout.write(self.style.SUCCESS(f'New Group {c} Successfully'))