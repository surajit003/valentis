from . import models
from . import serializers
from rest_framework import viewsets, permissions
from rest_framework import filters

class modelsViewSet(viewsets.ModelViewSet):
    """ViewSet for the models class"""

    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('patient_no', 'first_name', 'last_name', 'ss_number', 'dob')

class allergiesviewset(viewsets.ModelViewSet):
    """ViewSet for the models class"""

    queryset = models.Allergies.objects.all()
    serializer_class = serializers.allergiesserializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('allergy_name')

class countyviewset(viewsets.ModelViewSet):
    """ViewSet for the models class"""

    queryset = models.County.objects.all()
    serializer_class = serializers.countyserializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('County')

class medicationhistoryviewset(viewsets.ModelViewSet):
    queryset = models.MedicationHistory.objects.all()
    serializer_class = serializers.medicationserializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('Disease')

class insurancecompanyviewset(viewsets.ModelViewSet):
    queryset = models.InsuranceCompanies.objects.all()
    serializer_class = serializers.insuranceserializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('Name')

