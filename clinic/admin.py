<<<<<<< HEAD
from django.contrib import admin
from django import forms
from .models import PatientVisit, Diagnosis

class PatientVisitAdminForm(forms.ModelForm):

    class Meta:
        model = PatientVisit
        fields = '__all__'


class PatientVisitAdmin(admin.ModelAdmin):
    form = PatientVisitAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'patient_no', 'radiology_no', 'notes', 'diagnosis', 'prescription_id', 'status', 'triage_id', 'examination', 'plan_of_managemnt', 'query_diagnosis', 'his_presenting_illness', 'attending_doctor','visit_id','diag_search']

admin.site.register(PatientVisit, PatientVisitAdmin)


class DiagnosisAdminForm(forms.ModelForm):

    class Meta:
        model = Diagnosis
        fields = '__all__'


class DiagnosisAdmin(admin.ModelAdmin):
    form = DiagnosisAdminForm
    list_display = ['created', 'last_updated', 'code', 'name']

admin.site.register(Diagnosis, DiagnosisAdmin)


=======
from django.contrib import admin
from django import forms
from .models import PatientVisit, Diagnosis

class PatientVisitAdminForm(forms.ModelForm):

    class Meta:
        model = PatientVisit
        fields = '__all__'


class PatientVisitAdmin(admin.ModelAdmin):
    form = PatientVisitAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'patient_no', 'radiology_no', 'notes', 'diagnosis', 'prescription_id', 'status', 'triage_id', 'examination', 'plan_of_managemnt', 'query_diagnosis', 'his_presenting_illness', 'attending_doctor','visit_id','diag_search']

admin.site.register(PatientVisit, PatientVisitAdmin)


class DiagnosisAdminForm(forms.ModelForm):

    class Meta:
        model = Diagnosis
        fields = '__all__'


class DiagnosisAdmin(admin.ModelAdmin):
    form = DiagnosisAdminForm
    list_display = ['created', 'last_updated', 'code', 'name']

admin.site.register(Diagnosis, DiagnosisAdmin)


>>>>>>> 037b6d71d45035c58b96fc5d43770f0b5c23cb0f
