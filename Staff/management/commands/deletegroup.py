from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.db.utils import IntegrityError
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission, User
from Staff.models.staff import *
from Patient.models.patient import *
from Department.models.department import *


class Command(BaseCommand):
    help = 'Delete Group'
    def add_arguments(self, parser):
        parser.add_argument('name', nargs='?', type=str)
    def handle(self, *args, **options):

        c = options['name']
        if c:
            try:
                group = Group.objects.get(name=c)
                group.delete()
            except:
                raise CommandError(f'Cannot delete {c} in Group List')
            self.stdout.write(self.style.SUCCESS(f'Group  {c} deleted Successfully'))
        else:
            for c in Group.objects.all():
                try:
                    c.delete()
                except :
                    raise CommandError(f'{c} deleted in Group List')
                self.stdout.write(self.style.SUCCESS(f'Group  {c} deleted successfully Successfully'))