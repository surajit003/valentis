import unittest
from django.urls import reverse
from django.test import Client
from .models import Nurse
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
    defaults["systolic"] = "systolic"
    defaults["diastolic"] = "diastolic"
    defaults["temperature"] = "temperature"
    defaults["oxygen_saturation"] = "oxygen_saturation"
    defaults["urinalysis"] = "urinalysis"
    defaults["heart_rate"] = "heart_rate"
    defaults["others"] = "others"
    defaults["attending_nurse"] = "attending_nurse"
    defaults["patient_no"] = "patient_no"
    defaults["first_name"] = "first_name"
    defaults["last_name"] = "last_name"
    defaults["middle_name"] = "middle_name"
    defaults.update(**kwargs)
    return Nurse.objects.create(**defaults)


class modelsViewTest(unittest.TestCase):
    '''
    Tests for Nurse
    '''
    def setUp(self):
        self.client = Client()

    def test_list_models(self):
        url = reverse('nurse_models_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_models(self):
        url = reverse('nurse_models_create')
        data = {
            "systolic": "systolic",
            "diastolic": "diastolic",
            "temperature": "temperature",
            "oxygen_saturation": "oxygen_saturation",
            "urinalysis": "urinalysis",
            "heart_rate": "heart_rate",
            "others": "others",
            "attending_nurse": "attending_nurse",
            "patient_no": "patient_no",

        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_models(self):
        models = create_models()
        url = reverse('nurse_models_detail', args=[models.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_models(self):
        models = create_models()
        data = {
            "systolic": "systolic",
            "diastolic": "diastolic",
            "temperature": "temperature",
            "oxygen_saturation": "oxygen_saturation",
            "urinalysis": "urinalysis",
            "heart_rate": "heart_rate",
            "others": "others",
            "attending_nurse": "attending_nurse",
            "patient_no": "patient_no",

        }
        url = reverse('nurse_models_update', args=[models.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


