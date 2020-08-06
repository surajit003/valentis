import unittest
from django.urls import reverse
from django.test import Client
from .models import PatientVisit
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


def create_patientvisit(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["patient_no"] = "23"
    # defaults["radiology_no"] = "radiology_no"
    defaults["notes"] = "notes"
    defaults["diagnosis"] = "diagnosis"
    # defaults["prescription_id"] = "prescription_id"
    defaults["status"] = "2"

    defaults["examination"] = "examination",
    defaults["plan_of_managemnt"] = "My plan of management is to x y z",
    defaults["query_diagnosis"] = "query_diagnosis?",
    defaults["his_presenting_illness"] = "History of presenting illness",
    defaults["attending_doctor"] = "Doctor Z",
    defaults.update(**kwargs)
    return PatientVisit.objects.create(**defaults)


class PatientVisitViewTest(unittest.TestCase):
    '''
    Tests for PatientVisit
    '''
    def setUp(self):
        self.client = Client()

    def test_list_patientvisit(self):
        url = reverse('clinic_patientvisit_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_patientvisit(self):
        url = reverse('clinic_patientvisit_create')
        data = {
            "name": "name",
            "patient_no": "23",
            "radiology_no": "radiology_no",
            "notes": "notes",
            "diagnosis": "diagnosis",
            # "prescription_id": "prescription_id",
            "status": "2",
            "examination":"examination",
            "plan_of_managemnt":"My plan of management is to x y z",
            "query_diagnosis":"query_diagnosis?",
            "his_presenting_illness":"History of presenting illness",
            "attending_doctor":"Doctor Z",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_patientvisit(self):
        patientvisit = create_patientvisit()
        self.assertEqual(PatientVisit.objects.get(patient_no=23).name, 'name')

    def test_update_patientvisit(self):
        patientvisit = create_patientvisit()
        data = {
            "name": "name",
            "patient_no": "23",
            "radiology_no": "radiology_no",
            "notes": "notes",
            "diagnosis": "diagnosis",
            # "prescription_id": "prescription_id",
            "status": "2",
            "examination":"examination",
            "plan_of_managemnt":"My plan of management is to x y z",
            "query_diagnosis":"query_diagnosis?",
            "his_presenting_illness":"History of presenting illness",
            "attending_doctor":"Doctor Z",
        }
        url = reverse('clinic_patientvisit_update', args=[patientvisit.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


