from django.db import models
from .department import Department

class Room(models.Model):
    name = models.CharField( max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    max_bed_num = models.IntegerField()

class Bed(models.Model):
    name = models.CharField(max_length=10)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
