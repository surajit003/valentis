from . import models
from . import serializers
from rest_framework import viewsets, permissions, filters

class PatientVisitViewSet(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.PatientVisit.objects.all()
    serializer_class = serializers.patientVisitSerializer
    permission_classes = [permissions.IsAuthenticated]



class DiagnosisViewSet(viewsets.ModelViewSet):
    """ViewSet for the models class"""

    queryset = models.Diagnosis.objects.all()
    serializer_class = serializers.DiagnosisSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('code', 'name')


class RadiologyResultsViewSet(viewsets.ModelViewSet):
    """ViewSet for the LabResults class"""

    queryset = models.Radiologylist.objects.all()
    serializer_class = serializers.RadiologytestsSerializer
    permission_classes = [permissions.IsAuthenticated]

