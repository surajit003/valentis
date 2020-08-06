
from . import models
from . import serializers
from rest_framework import viewsets, permissions


class modelsViewSet(viewsets.ModelViewSet):
    """ViewSet for the models class"""

    queryset = models.Nurse.objects.all()
    serializer_class = serializers.modelsSerializer
    permission_classes = [permissions.IsAuthenticated]
