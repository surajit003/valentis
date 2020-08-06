from django import forms
from .models import PatientVisit


class PatientVisitForm(forms.ModelForm):
    class Meta:
        model = PatientVisit
        fields = ['name', 'patient_no', 'radiology_no', 'notes', 'diagnosis', 'status', 'examination', 'plan_of_managemnt','diag_search', 'query_diagnosis', 'his_presenting_illness']

