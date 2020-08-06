from django.contrib import admin
from django import forms
from .models import Message

class MessageAdminForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'


class MessageAdmin(admin.ModelAdmin):
    form = MessageAdminForm
    list_display = ['name', 'message_no', 'created', 'last_updated', 'subject', 'body', 'sent_at', 'read_at', 'replied_at', 'sender', 'recipient', 'sender_archived', 'recipient_archived', 'sender_deleted_at', 'recipient_deleted_at']
    readonly_fields = ['name', 'message_no', 'created', 'last_updated', 'sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived', 'sender_deleted_at', 'recipient_deleted_at']

admin.site.register(Message, MessageAdmin)


