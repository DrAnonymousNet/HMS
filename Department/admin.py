from django.contrib import admin
from .models.department import *
from .models.inventory import *

admin.site.register(Bed)
admin.site.register(Department)
admin.site.register(Room)
# Register your models here.
