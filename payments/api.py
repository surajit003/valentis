from . import models
from . import serializers
from rest_framework import viewsets, permissions
from rest_framework import filters

class member_infoViewSet(viewsets.ModelViewSet):
    """ViewSet for the member_info class"""

    queryset = models.member_info.objects.all()
    serializer_class = serializers.member_infoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('member_no', 'first_name', 'surname', 'other_name')


class member_benefitsViewSet(viewsets.ModelViewSet):
    """ViewSet for the member_benefits class"""

    queryset = models.member_benefits.objects.all()
    serializer_class = serializers.member_benefitsSerializer
    # permission_classes = [permissions.IsAuthenticated]




class member_anniversaryViewSet(viewsets.ModelViewSet):
    """ViewSet for the member_anniversary class"""

    queryset = models.member_anniversary.objects.all()
    serializer_class = serializers.member_anniversarySerializer
    # permission_classes = [permissions.IsAuthenticated]


class member_acceptanceViewSet(viewsets.ModelViewSet):
    """ViewSet for the member_acceptance class"""

    queryset = models.member_acceptance.objects.all()
    serializer_class = serializers.member_acceptanceSerializer
    # permission_classes = [permissions.IsAuthenticated]


class principal_applicantViewSet(viewsets.ModelViewSet):
    """ViewSet for the principal_applicant class"""

    queryset = models.principal_applicant.objects.all()
    serializer_class = serializers.principal_applicantSerializer
    # permission_classes = [permissions.IsAuthenticated]


class pre_authorizationViewSet(viewsets.ModelViewSet):
    """ViewSet for the pre_authorization class"""

    queryset = models.pre_authorization.objects.all()
    serializer_class = serializers.pre_authorizationSerializer
    # permission_classes = [permissions.IsAuthenticated]


class providerViewSet(viewsets.ModelViewSet):
    """ViewSet for the provider class"""

    queryset = models.provider.objects.all()
    serializer_class = serializers.providerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class cashViewSet(viewsets.ModelViewSet):
    """ViewSet for the cash class"""

    queryset = models.cash.objects.all()
    serializer_class = serializers.cashSerializer
    # permission_classes = [permissions.IsAuthenticated]



class memberinfosanlamviewset(viewsets.ModelViewSet):
    """ViewSet for the cash class"""

    queryset = models.memberinfosanlamdatabase.objects.all()
    serializer_class = serializers.memberinfosanlamserializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('SURNAME','MEMBER_NO',)



