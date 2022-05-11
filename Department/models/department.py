from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to="profile_picture")
    about = models.CharField(max_length=10)