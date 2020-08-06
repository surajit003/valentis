from django.contrib import admin
from django import forms
from .models import Nurse

class ModelsAdminForm(forms.ModelForm):

    class Meta:
        model = Nurse
        fields = '__all__'


class ModelsAdmin(admin.ModelAdmin):
    form = ModelsAdminForm
    list_display = [f.name for f in Nurse._meta.fields]

admin.site.register(Nurse, ModelsAdmin)


