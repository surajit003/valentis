from django import forms
from .models import Medication


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['patient_no', 'patient_name', 'address', 'phone_number', 'prescription','physical_address']


