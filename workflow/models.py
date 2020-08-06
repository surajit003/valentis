from django.urls import reverse
from django.db.models import *
from django.db import models as models
from django.utils.translation import ugettext_lazy as _
import datetime
from django.conf import settings
# from account.models import CustomUser as User

class Message(models.Model):
    # Fields
    SUBJECT_MAX_LENGTH = 120

    name = CharField(max_length=255)
    message_no = AutoField(primary_key=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    subject = CharField(_("subject"), max_length=SUBJECT_MAX_LENGTH)
    body = TextField(_("body"), blank=True)
    sent_at = DateTimeField(auto_now=True, editable=False)
    read_at = DateTimeField(_("read at"), null=True, blank=True)
    replied_at = DateTimeField(_("replied at"), null=True, blank=True)
    sender_archived = BooleanField(_("archived by sender"), default=False)
    recipient_archived = BooleanField(_("archived by recipient"), default=False)
    sender_deleted_at = DateTimeField(_("deleted by sender at"), null=True, blank=True)
    recipient_deleted_at = DateTimeField(_("deleted by recipient at"), null=True, blank=True)

    # Relationship Fields
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages+',
                               null=True, blank=True, verbose_name=_("sender"))
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages+',
                                  null=True, blank=True, verbose_name=_("recipient"))

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.receipt

    def __str__(self):
        return "from {0} to {1}:\nsubject {2}".format(self.sender, self.recipient, self.subject)

    def get_absolute_url(self):
        return reverse('workflow_message_list')

    def get_update_url(self):
        return reverse('workflow_message_list')


class WorkflowManager:
    def inbox(self, user):
        """
        Return accepted messages received by a user but not marked as archived or deleted.
        """
        print("getting your messages")
        return Message.objects.filter(Q(recipient=user)).exclude(sender_archived=True).filter(sender_deleted_at__isnull=True)

    def inbox_unread_count(self, user):
        """
        Return the number of unread messages for a user.

        Designed for context_processors.py and templatetags/postman_tags.py

        """
        return self.inbox(user).filter(read_at__isnull=True).count()

    def sent(self, user, **kwargs):
        """
        Return all messages sent by a user but not marked as archived or deleted.
        """
        return Message.objects.filter(Q(sender=user)).exclude(sender_archived=True) #.filter(sender_deleted_at__isnull=True)