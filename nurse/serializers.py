from . import models

from rest_framework import serializers


class modelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Nurse
        exclude = ('patient_no', 'created', 'triage_id', 'last_updated', 'slug')


