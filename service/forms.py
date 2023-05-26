from django import forms
from .models import *

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'
        widgets ={
            'type': forms.RadioSelect()
        }

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = '__all__'