from django.contrib import admin
from django import forms
from .models import Patient, Allergies, County, Child


class PatientAdminForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm

    list_display = [f.name for f in Patient._meta.fields]

admin.site.register(Patient, PatientAdmin)


class ChildAdminForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = '__all__'


class ChildAdmin(admin.ModelAdmin):
    form = ChildAdminForm

    list_display = [f.name for f in Child._meta.fields]

admin.site.register(Child, ChildAdmin)