import unittest
from django.urls import reverse
from django.test import Client
from .models import member_info, member_benefits, member_anniversary, member_acceptance, principal_applicant, pre_authorization, provider, cash
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


def create_member_info(**kwargs):
    defaults = {}
    defaults["family_no"] = "family_no"
    defaults["member_no"] = "member_no"
    defaults["surname"] = "surname"
    defaults["first_name"] = "first_name"
    defaults["other_name"] = "other_name"
    defaults["dob"] = "dob"
    defaults["user_id"] = "user_id"
    defaults["date_entered"] = "date_entered"
    defaults["cancelled"] = "cancelled"
    defaults["employment_no"] = "employment_no"
    defaults["gender"] = "gender"
    defaults["passport_no"] = "passport_no"
    defaults.update(**kwargs)
    return member_info.objects.create(**defaults)


def create_member_benefits(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["member_no"] = "member_no"
    defaults["limit"] = "limit"
    defaults["sharing"] = "sharing"
    defaults["anniv"] = "anniv"
    defaults["suspended"] = "suspended"
    defaults["expense"] = "expense"
    defaults["idx"] = "idx"
    defaults["balance"] = "balance"
    defaults.update(**kwargs)
    return member_benefits.objects.create(**defaults)


def create_member_anniversary(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["member_no"] = "member_no"
    defaults["start_date"] = "start_date"
    defaults["end_date"] = "end_date"
    defaults["anniv"] = "anniv"
    defaults.update(**kwargs)
    return member_anniversary.objects.create(**defaults)


def create_member_acceptance(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["member_no"] = "member_no"
    defaults["status"] = "status"
    defaults["status_date"] = "status_date"
    defaults["user_id"] = "user_id"
    defaults["date_entered"] = "date_entered"
    defaults.update(**kwargs)
    return member_acceptance.objects.create(**defaults)


def create_principal_applicant(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["family_no"] = "family_no"
    defaults["first_name"] = "first_name"
    defaults["postal_add"] = "postal_add"
    defaults["town"] = "town"
    defaults["email"] = "email"
    defaults["other_names"] = "other_names"
    defaults["corp_id"] = "corp_id"
    defaults["mobile_no"] = "mobile_no"
    defaults["family_size"] = "family_size"
    defaults["user_id"] = "user_id"
    defaults["category"] = "category"
    defaults.update(**kwargs)
    return principal_applicant.objects.create(**defaults)


def create_pre_authorization(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["member_no"] = "member_no"
    defaults["provider"] = "provider"
    defaults["date_reported"] = "date_reported"
    defaults["reported_by"] = "reported_by"
    defaults["authorized_by"] = "authorized_by"
    defaults["date_authorized"] = "date_authorized"
    defaults["pre_diagnosis"] = "pre_diagnosis"
    defaults["authority_type"] = "authority_type"
    defaults["ward"] = "ward"
    defaults["available_limit"] = "available_limit"
    defaults["admit_days"] = "admit_days"
    defaults["reserve"] = "reserve"
    defaults["notes"] = "notes"
    defaults["anniv"] = "anniv"
    # defaults["auth_batch_no"] = "auth_batch_no"
    defaults["day_bed_charge"] = "day_bed_charge"
    defaults["date_admitted"] = "date_admitted"
    defaults["code"] = "code"
    defaults.update(**kwargs)
    return pre_authorization.objects.create(**defaults)


def create_provider(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["code"] = "code"
    defaults["provider"] = "provider"
    defaults.update(**kwargs)
    return provider.objects.create(**defaults)


def create_cash(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["items"] = "items"
    defaults["amount_payed"] = "amount_payed"
    defaults["total_cost"] = "total_cost"
    defaults["balance"] = "balance"
    defaults.update(**kwargs)
    return cash.objects.create(**defaults)


class member_infoViewTest(unittest.TestCase):
    '''
    Tests for member_info
    '''
    def setUp(self):
        self.client = Client()

    def test_list_member_info(self):
        url = reverse('payments_member_info_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_member_info(self):
        url = reverse('payments_member_info_create')
        data = {
            "family_no": "family_no",
            "member_no": "member_no",
            "surname": "surname",
            "first_name": "first_name",
            "other_name": "other_name",
            "dob": "dob",
            "user_id": "user_id",
            "date_entered": "date_entered",
            "cancelled": "cancelled",
            "employment_no": "employment_no",
            "gender": "gender",
            "passport_no": "passport_no",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_member_info(self):
        member_info = create_member_info()
        url = reverse('payments_member_info_detail', args=[member_info.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_member_info(self):
        member_info = create_member_info()
        data = {
            "family_no": "family_no",
            "member_no": "member_no",
            "surname": "surname",
            "first_name": "first_name",
            "other_name": "other_name",
            "dob": "dob",
            "user_id": "user_id",
            "date_entered": "date_entered",
            "cancelled": "cancelled",
            "employment_no": "employment_no",
            "gender": "gender",
            "passport_no": "passport_no",
        }
        url = reverse('payments_member_info_update', args=[member_info.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class member_benefitsViewTest(unittest.TestCase):
    '''
    Tests for member_benefits
    '''
    def setUp(self):
        self.client = Client()

    def test_list_member_benefits(self):
        url = reverse('payments_member_benefits_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_member_benefits(self):
        url = reverse('payments_member_benefits_create')
        data = {
            "name": "name",
            "member_no": "member_no",
            "limit": "limit",
            "sharing": "sharing",
            "anniv": "anniv",
            "suspended": "suspended",
            "expense": "expense",
            "idx": "idx",
            "balance": "balance",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_member_benefits(self):
        member_benefits = create_member_benefits()
        url = reverse('payments_member_benefits_detail', args=[member_benefits.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_member_benefits(self):
        member_benefits = create_member_benefits()
        data = {
            "name": "name",
            "member_no": "member_no",
            "limit": "limit",
            "sharing": "sharing",
            "anniv": "anniv",
            "suspended": "suspended",
            "expense": "expense",
            "idx": "idx",
            "balance": "balance",
        }
        url = reverse('payments_member_benefits_update', args=[member_benefits.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class member_anniversaryViewTest(unittest.TestCase):
    '''
    Tests for member_anniversary
    '''
    def setUp(self):
        self.client = Client()

    def test_list_member_anniversary(self):
        url = reverse('payments_member_anniversary_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_member_anniversary(self):
        url = reverse('payments_member_anniversary_create')
        data = {
            "name": "name",
            "member_no": "member_no",
            "start_date": "start_date",
            "end_date": "end_date",
            "anniv": "anniv",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_member_anniversary(self):
        member_anniversary = create_member_anniversary()
        url = reverse('payments_member_anniversary_detail', args=[member_anniversary.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_member_anniversary(self):
        member_anniversary = create_member_anniversary()
        data = {
            "name": "name",
            "member_no": "member_no",
            "start_date": "start_date",
            "end_date": "end_date",
            "anniv": "anniv",
        }
        url = reverse('payments_member_anniversary_update', args=[member_anniversary.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class member_acceptanceViewTest(unittest.TestCase):
    '''
    Tests for member_acceptance
    '''
    def setUp(self):
        self.client = Client()

    def test_list_member_acceptance(self):
        url = reverse('payments_member_acceptance_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_member_acceptance(self):
        url = reverse('payments_member_acceptance_create')
        data = {
            "name": "name",
            "member_no": "member_no",
            "status": "status",
            "status_date": "status_date",
            "user_id": "user_id",
            "date_entered": "date_entered",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_member_acceptance(self):
        member_acceptance = create_member_acceptance()
        url = reverse('payments_member_acceptance_detail', args=[member_acceptance.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_member_acceptance(self):
        member_acceptance = create_member_acceptance()
        data = {
            "name": "name",
            "member_no": "member_no",
            "status": "status",
            "status_date": "status_date",
            "user_id": "user_id",
            "date_entered": "date_entered",
        }
        url = reverse('payments_member_acceptance_update', args=[member_acceptance.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class principal_applicantViewTest(unittest.TestCase):
    '''
    Tests for principal_applicant
    '''
    def setUp(self):
        self.client = Client()

    def test_list_principal_applicant(self):
        url = reverse('payments_principal_applicant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_principal_applicant(self):
        url = reverse('payments_principal_applicant_create')
        data = {
            "name": "name",
            "family_no": "family_no",
            "first_name": "first_name",
            "postal_add": "postal_add",
            "town": "town",
            "email": "email",
            "other_names": "other_names",
            "corp_id": "corp_id",
            "mobile_no": "mobile_no",
            "family_size": "family_size",
            "user_id": "user_id",
            "category": "category",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_principal_applicant(self):
        principal_applicant = create_principal_applicant()
        url = reverse('payments_principal_applicant_detail', args=[principal_applicant.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_principal_applicant(self):
        principal_applicant = create_principal_applicant()
        data = {
            "name": "name",
            "family_no": "family_no",
            "first_name": "first_name",
            "postal_add": "postal_add",
            "town": "town",
            "email": "email",
            "other_names": "other_names",
            "corp_id": "corp_id",
            "mobile_no": "mobile_no",
            "family_size": "family_size",
            "user_id": "user_id",
            "category": "category",
        }
        url = reverse('payments_principal_applicant_update', args=[principal_applicant.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class pre_authorizationViewTest(unittest.TestCase):
    '''
    Tests for pre_authorization
    '''
    def setUp(self):
        self.client = Client()

    def test_list_pre_authorization(self):
        url = reverse('payments_pre_authorization_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pre_authorization(self):
        url = reverse('payments_pre_authorization_create')
        data = {
            "name": "name",
            "member_no": "member_no",
            "provider": "provider",
            "date_reported": "date_reported",
            "reported_by": "reported_by",
            "authorized_by": "authorized_by",
            "date_authorized": "date_authorized",
            "pre_diagnosis": "pre_diagnosis",
            "authority_type": "authority_type",
            "ward": "ward",
            "available_limit": "available_limit",
            "admit_days": "admit_days",
            "reserve": "reserve",
            "notes": "notes",
            "anniv": "anniv",
            # "auth_batch_no": "auth_batch_no",
            "day_bed_charge": "day_bed_charge",
            "date_admitted": "date_admitted",
            "code": "code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pre_authorization(self):
        pre_authorization = create_pre_authorization()
        url = reverse('payments_pre_authorization_detail', args=[pre_authorization.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pre_authorization(self):
        pre_authorization = create_pre_authorization()
        data = {
            "name": "name",
            "member_no": "member_no",
            "provider": "provider",
            "date_reported": "date_reported",
            "reported_by": "reported_by",
            "authorized_by": "authorized_by",
            "date_authorized": "date_authorized",
            "pre_diagnosis": "pre_diagnosis",
            "authority_type": "authority_type",
            "ward": "ward",
            "available_limit": "available_limit",
            "admit_days": "admit_days",
            "reserve": "reserve",
            "notes": "notes",
            "anniv": "anniv",
            # "auth_batch_no": "auth_batch_no",
            "day_bed_charge": "day_bed_charge",
            "date_admitted": "date_admitted",
            "code": "code",
        }
        url = reverse('payments_pre_authorization_update', args=[pre_authorization.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class providerViewTest(unittest.TestCase):
    '''
    Tests for provider
    '''
    def setUp(self):
        self.client = Client()

    def test_list_provider(self):
        url = reverse('payments_provider_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_provider(self):
        url = reverse('payments_provider_create')
        data = {
            "name": "name",
            "code": "code",
            "provider": "provider",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_provider(self):
        provider = create_provider()
        url = reverse('payments_provider_detail', args=[provider.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_provider(self):
        provider = create_provider()
        data = {
            "name": "name",
            "code": "code",
            "provider": "provider",
        }
        url = reverse('payments_provider_update', args=[provider.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class cashViewTest(unittest.TestCase):
    '''
    Tests for cash
    '''
    def setUp(self):
        self.client = Client()

    def test_list_cash(self):
        url = reverse('payments_cash_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_cash(self):
        url = reverse('payments_cash_create')
        data = {
            "name": "name",
            "items": "items",
            "amount_payed": "amount_payed",
            "total_cost": "total_cost",
            "balance": "balance",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_cash(self):
        cash = create_cash()
        url = reverse('payments_cash_detail', args=[cash.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_cash(self):
        cash = create_cash()
        data = {
            "name": "name",
            "items": "items",
            "amount_payed": "amount_payed",
            "total_cost": "total_cost",
            "balance": "balance",
        }
        url = reverse('payments_cash_update', args=[cash.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


