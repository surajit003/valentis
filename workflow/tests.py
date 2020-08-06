import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_message(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["message_no"] = "message_no"
    defaults["subject"] = "subject"
    defaults["body"] = "body"
    defaults["sent_at"] = "sent_at"
    defaults["read_at"] = "read_at"
    defaults["replied_at"] = "replied_at"
    defaults["sender_archived"] = "sender_archived"
    defaults["recipient_archived"] = "recipient_archived"
    defaults["sender_deleted_at"] = "sender_deleted_at"
    defaults["recipient_deleted_at"] = "recipient_deleted_at"
    defaults.update(**kwargs)
    if "sender" not in defaults:
        defaults["sender"] = create_user()
    return Message.objects.create(**defaults)


class MessageViewTest(unittest.TestCase):
    '''
    Tests for Message
    '''
    def setUp(self):
        self.client = Client()

    def test_list_message(self):
        url = reverse('workflow_message_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_message(self):
        url = reverse('workflow_message_create')
        data = {
            "name": "name",
            "message_no": "message_no",
            "subject": "subject",
            "body": "body",
            "sent_at": "sent_at",
            "read_at": "read_at",
            "replied_at": "replied_at",
            "sender_archived": "sender_archived",
            "recipient_archived": "recipient_archived",
            "sender_deleted_at": "sender_deleted_at",
            "recipient_deleted_at": "recipient_deleted_at",
            "sender": create_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_message(self):
        message = create_message()
        url = reverse('workflow_message_detail', args=[message.message_no,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_message(self):
        message = create_message()
        data = {
            "name": "name",
            "message_no": "message_no",
            "subject": "subject",
            "body": "body",
            "sent_at": "sent_at",
            "read_at": "read_at",
            "replied_at": "replied_at",
            "sender_archived": "sender_archived",
            "recipient_archived": "recipient_archived",
            "sender_deleted_at": "sender_deleted_at",
            "recipient_deleted_at": "recipient_deleted_at",
            "sender": create_user().pk,
        }
        url = reverse('workflow_message_update', args=[message.message_no,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


