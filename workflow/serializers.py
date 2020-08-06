from . import models

from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = (
            'message_no',
            'name', 
            'created', 
            'last_updated', 
            'subject', 
            'body', 
            'sent_at', 
            'read_at', 
            'replied_at', 
            'sender_archived', 
            'recipient_archived', 
            'sender_deleted_at', 
            'recipient_deleted_at', 
        )


