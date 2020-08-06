from . import models
from . import serializers
from rest_framework import viewsets, permissions


class LabsViewSet(viewsets.ModelViewSet):
    """ViewSet for the tests class"""

    queryset = models.Labs.objects.all()
    serializer_class = serializers.LabsSerializer
    permission_classes = [permissions.IsAuthenticated]


class RadiologyViewSet(viewsets.ModelViewSet):
    """ViewSet for the radiology class"""

    queryset = models.Radiology.objects.all()
    serializer_class = serializers.RadiologySerializer
    permission_classes = [permissions.IsAuthenticated]



class RadiologyResultViewSet(viewsets.ModelViewSet):
    """ViewSet for the RadiologyResult class"""

    queryset = models.RadiologyResult.objects.all()
    serializer_class = serializers.RadiologyResultSerializer
    permission_classes = [permissions.IsAuthenticated]


class LabResultsViewSet(viewsets.ModelViewSet):
    """ViewSet for the LabResults class"""

    queryset = models.LabResults.objects.all()
    serializer_class = serializers.LabResultsSerializer
    permission_classes = [permissions.IsAuthenticated]

