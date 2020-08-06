from . import models

from rest_framework import serializers


class patientVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PatientVisit
        fields = '__all__'


class DiagnosisSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Diagnosis
        fields = (
            'code',
            'name',
        )


class RadiologytestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Radiologylist
        fields = (
            'group',
            'modality',
            'tests',

        )




