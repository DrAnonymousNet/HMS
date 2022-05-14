from django.db import models
from .department import Department
from django.dispatch import Signal

class Room(models.Model):
    name = models.CharField( max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    max_bed_num = models.IntegerField()

    def __str__(self):
        return self.name



class Bed(models.Model):
    status_choice = [
        ("Free", "Free"),
        ("Occupied", "Occupied")
    ]
    name = models.CharField(max_length=10)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(max_length= 10, choices= status_choice, default= 1)


    def __str__(self):
        return self.name

