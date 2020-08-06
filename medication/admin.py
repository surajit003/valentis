from django.contrib import admin
from django import forms
from .models import Medication

class MedicationAdminForm(forms.ModelForm):

    class Meta:
        model = Medication
        fields = '__all__'


class MedicationAdmin(admin.ModelAdmin):
    form = MedicationAdminForm
    list_display = ['slug', 'created', 'last_updated', 'prescription_id', 'patient_no', 'patient_name', 'address', 'email', 'phone_number', 'signature', 'prescription','triage_id']

admin.site.register(Medication, MedicationAdmin)


