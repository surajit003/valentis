from . import models
from . import serializers
from rest_framework import viewsets, permissions


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Message class"""

    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


