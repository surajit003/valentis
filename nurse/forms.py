from django import forms
from .models import Nurse


class ModelsForm(forms.ModelForm):
    class Meta:
        model = Nurse

        exclude = ('created', 'triage_id', 'last_updated', 'slug')

