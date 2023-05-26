from django import forms
from .models import *

class AutoCarForm(forms.ModelForm):
    class Meta:
        model = AutoCar
        fields = '__all__'