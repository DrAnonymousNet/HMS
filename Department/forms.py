from django import forms
from .models.inventory import Room, Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
