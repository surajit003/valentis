import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Medication
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


def create_models(**kwargs):
    defaults = {}
    defaults["prescription_id"] = "prescription_id"
    defaults["patient_no"] = "patient_no"
    defaults["patient_name"] = "patient_name"
    defaults["address"] = "address"
    defaults["phone_number"] = "phone_number"
    defaults["signature"] = "signature"
    defaults["prescription"] = "prescription"
    defaults.update(**kwargs)
    return Medication.objects.create(**defaults)


class modelsViewTest(unittest.TestCase):
    '''
    Tests for models
    '''
    def setUp(self):
        self.client = Client()

    def test_list_models(self):
        url = reverse('medication_models_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_models(self):
        url = reverse('medication_models_create')
        data = {
            "prescription_id": "prescription_id",
            "patient_no": "patient_no",
            "patient_name": "patient_name",
            "address": "address",
            "phone_number": "phone_number",
            "signature": "signature",
            "prescription": "prescription",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_models(self):
        models = create_models()
        url = reverse('medication_models_detail', args=[models.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_models(self):
        models = create_models()
        data = {
            "prescription_id": "prescription_id",
            "patient_no": "patient_no",
            "patient_name": "patient_name",
            "address": "address",
            "phone_number": "phone_number",
            "signature": "signature",
            "prescription": "prescription",
        }
        url = reverse('medication_models_update', args=[models.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


