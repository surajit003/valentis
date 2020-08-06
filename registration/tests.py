import unittest
from django.urls import reverse
from django.test import Client
from .models import Patient as models
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
    defaults["patient_no"] = "patient_no"
    defaults["first_name"] = "first_name"
    defaults["middle_name"] = "middle_name"
    defaults["last_name"] = "last_name"
    defaults["gender"] = "gender"
    defaults["street_name"] = "street_name"
    defaults["apartment_name"] = "apartment_name"
    defaults["postal_code"] = "postal_code"
    defaults["postal_address"] = "postal_address"
    defaults["city"] = "city"
    defaults["country"] = "country"
    defaults["age"] = "age"
    defaults["next_of_kin"] = "next_of_kin"
    defaults["n_of_kin_rel"] = "n_of_kin_rel"
    defaults["email"] = "email"
    defaults["phone"] = "phone"
    defaults["primary_insurance"] = "primary_insurance"
    defaults["secondary_insurance"] = "secondary_insurance"
    defaults["pri_ins_sub"] = "pri_ins_sub"
    defaults["sec_ins_sub"] = "sec_ins_sub"
    defaults["other_ins_subscriber"] = "other_ins_subscriber"
    defaults["subscriber_relationship"] = "subscriber_relationship"
    defaults["sub_address"] = "sub_address"
    defaults["ss_number"] = "ss_number"
    defaults["sub_ss_number"] = "sub_ss_number"
    defaults["alt_phone"] = "alt_phone"
    defaults["sub_work_phone"] = "sub_work_phone"
    defaults["dob"] = "dob"
    defaults["sub_dob"] = "sub_dob"
    defaults["sub_employer"] = "sub_employer"

    defaults["occupation"] = "occupation"
    defaults["marital_status"] = "marital_status"
    defaults["spouse"] = "spouse"
    defaults["no_children"] = "no_children"
    defaults["childrens"] = "childrens"
    defaults["prev_docs"] = "prev_docs"
    defaults["medical_information"] = "medical_information"
    defaults["alergies"] = "alergies"
    defaults["preferred_pharmacy"] = "preferred_pharmacy"
    defaults["last_phys_examination"] = "last_phys_examination"
    defaults["last_blood_work"] = "last_blood_work"
    defaults["last_colonoscopy"] = "last_colonoscopy"
    defaults["last_tetanus_shot"] = "last_tetanus_shot"
    defaults["last_menstrual"] = "last_menstrual"
    defaults["last_pap_smear"] = "last_pap_smear"
    defaults["last_mammogram"] = "last_mammogram"
    defaults["dexa"] = "dexa"
    defaults["no_pregnancies"] = "no_pregnancies"
    defaults["miscourages"] = "miscourages"
    defaults["living_children"] = "living_children"
    defaults["methods_of_contraception"] = "methods_of_contraception"
    defaults["surgeries"] = "surgeries"
    defaults["genetic_diseases"] = "genetic_diseases"
    defaults["if_smoker"] = "if_smoker"
    defaults["cigar_per_day"] = "cigar_per_day"
    defaults["no_of_yr_smoking"] = "no_of_yr_smoking"
    defaults["if_chew_tobacco"] = "if_chew_tobacco"
    defaults["yrs_chewing_tobacco"] = "yrs_chewing_tobacco"
    defaults["if_quit_before"] = "if_quit_before"
    defaults["tobacco_quit_duration"] = "tobacco_quit_duration"
    defaults["if_drink_alcohol"] = "if_drink_alcohol"
    defaults["alocohol_type"] = "alocohol_type"
    defaults["alcohol_frequency"] = "alcohol_frequency"
    defaults["if_drug_used"] = "if_drug_used"
    defaults["drug_type"] = "drug_type"
    defaults["when_drug_used"] = "when_drug_used"
    defaults["if_exercise"] = "if_exercise"
    defaults["exercise_freq"] = "exercise_freq"
    defaults["if_special_diet"] = "if_special_diet"
    defaults["special_diet"] = "special_diet"
    defaults["if_use_caffein"] = "if_use_caffein"
    defaults["caffein_daily_amt"] = "caffein_daily_amt"
    defaults["is_sadder"] = "is_sadder"
    defaults["if_lost_interest"] = "if_lost_interest"
    defaults["have_will"] = "have_will"
    defaults.update(**kwargs)
    return models.objects.create(**defaults)


class modelsViewTest(unittest.TestCase):
    '''
    Tests for models
    '''
    def setUp(self):
        self.client = Client()

    def test_list_models(self):
        url = reverse('registration_models_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_models(self):
        url = reverse('registration_models_create')
        data = {
            "patient_no": "patient_no",
            "first_name": "first_name",
            "middle_name": "middle_name",
            "last_name": "last_name",
            "gender": "gender",
            "street_name": "street_name",
            "apartment_name": "apartment_name",
            "postal_code": "postal_code",
            "postal_address": "postal_address",
            "city": "city",
            "country": "country",
            "age": "age",
            "next_of_kin": "next_of_kin",
            "n_of_kin_rel": "n_of_kin_rel",
            "email": "email",
            "phone": "phone",
            "primary_insurance": "primary_insurance",
            "secondary_insurance": "secondary_insurance",
            "pri_ins_sub": "pri_ins_sub",
            "sec_ins_sub": "sec_ins_sub",
            "other_ins_subscriber": "other_ins_subscriber",
            "subscriber_relationship": "subscriber_relationship",
            "sub_address": "sub_address",
            "ss_number": "ss_number",
            "sub_ss_number": "sub_ss_number",
            "alt_phone": "alt_phone",
            "sub_work_phone": "sub_work_phone",
            "dob": "dob",
            "sub_dob": "sub_dob",
            "sub_employer": "sub_employer",

            "occupation": "occupation",
            "marital_status": "marital_status",
            "spouse": "spouse",
            "no_children": "no_children",
            "childrens": "childrens",
            "prev_docs": "prev_docs",
            "medical_information": "medical_information",
            "alergies": "alergies",
            "preferred_pharmacy": "preferred_pharmacy",
            "last_phys_examination": "last_phys_examination",
            "last_blood_work": "last_blood_work",
            "last_colonoscopy": "last_colonoscopy",
            "last_tetanus_shot": "last_tetanus_shot",
            "last_menstrual": "last_menstrual",
            "last_pap_smear": "last_pap_smear",
            "last_mammogram": "last_mammogram",
            "dexa": "dexa",
            "no_pregnancies": "no_pregnancies",
            "miscourages": "miscourages",
            "living_children": "living_children",
            "methods_of_contraception": "methods_of_contraception",
            "surgeries": "surgeries",
            "genetic_diseases": "genetic_diseases",
            "if_smoker": "if_smoker",
            "cigar_per_day": "cigar_per_day",
            "no_of_yr_smoking": "no_of_yr_smoking",
            "if_chew_tobacco": "if_chew_tobacco",
            "yrs_chewing_tobacco": "yrs_chewing_tobacco",
            "if_quit_before": "if_quit_before",
            "tobacco_quit_duration": "tobacco_quit_duration",
            "if_drink_alcohol": "if_drink_alcohol",
            "alocohol_type": "alocohol_type",
            "alcohol_frequency": "alcohol_frequency",
            "if_drug_used": "if_drug_used",
            "drug_type": "drug_type",
            "when_drug_used": "when_drug_used",
            "if_exercise": "if_exercise",
            "exercise_freq": "exercise_freq",
            "if_special_diet": "if_special_diet",
            "special_diet": "special_diet",
            "if_use_caffein": "if_use_caffein",
            "caffein_daily_amt": "caffein_daily_amt",
            "is_sadder": "is_sadder",
            "if_lost_interest": "if_lost_interest",
            "have_will": "have_will",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_models(self):
        models = create_models()
        url = reverse('registration_patients_detail', args=[models.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_models(self):
        models = create_models()
        data = {
            "patient_no": "patient_no",
            "first_name": "first_name",
            "middle_name": "middle_name",
            "last_name": "last_name",
            "gender": "gender",
            "street_name": "street_name",
            "apartment_name": "apartment_name",
            "postal_code": "postal_code",
            "postal_address": "postal_address",
            "city": "city",
            "country": "country",
            "age": "age",
            "next_of_kin": "next_of_kin",
            "n_of_kin_rel": "n_of_kin_rel",
            "email": "email",
            "phone": "phone",
            "primary_insurance": "primary_insurance",
            "secondary_insurance": "secondary_insurance",
            "pri_ins_sub": "pri_ins_sub",
            "sec_ins_sub": "sec_ins_sub",
            "other_ins_subscriber": "other_ins_subscriber",
            "subscriber_relationship": "subscriber_relationship",
            "sub_address": "sub_address",
            "ss_number": "ss_number",
            "sub_ss_number": "sub_ss_number",
            "alt_phone": "alt_phone",
            "sub_work_phone": "sub_work_phone",
            "dob": "dob",
            "sub_dob": "sub_dob",
            "sub_employer": "sub_employer",

            "occupation": "occupation",
            "marital_status": "marital_status",
            "spouse": "spouse",
            "no_children": "no_children",
            "childrens": "childrens",
            "prev_docs": "prev_docs",
            "medical_information": "medical_information",
            "alergies": "alergies",
            "preferred_pharmacy": "preferred_pharmacy",
            "last_phys_examination": "last_phys_examination",
            "last_blood_work": "last_blood_work",
            "last_colonoscopy": "last_colonoscopy",
            "last_tetanus_shot": "last_tetanus_shot",
            "last_menstrual": "last_menstrual",
            "last_pap_smear": "last_pap_smear",
            "last_mammogram": "last_mammogram",
            "dexa": "dexa",
            "no_pregnancies": "no_pregnancies",
            "miscourages": "miscourages",
            "living_children": "living_children",
            "methods_of_contraception": "methods_of_contraception",
            "surgeries": "surgeries",
            "genetic_diseases": "genetic_diseases",
            "if_smoker": "if_smoker",
            "cigar_per_day": "cigar_per_day",
            "no_of_yr_smoking": "no_of_yr_smoking",
            "if_chew_tobacco": "if_chew_tobacco",
            "yrs_chewing_tobacco": "yrs_chewing_tobacco",
            "if_quit_before": "if_quit_before",
            "tobacco_quit_duration": "tobacco_quit_duration",
            "if_drink_alcohol": "if_drink_alcohol",
            "alocohol_type": "alocohol_type",
            "alcohol_frequency": "alcohol_frequency",
            "if_drug_used": "if_drug_used",
            "drug_type": "drug_type",
            "when_drug_used": "when_drug_used",
            "if_exercise": "if_exercise",
            "exercise_freq": "exercise_freq",
            "if_special_diet": "if_special_diet",
            "special_diet": "special_diet",
            "if_use_caffein": "if_use_caffein",
            "caffein_daily_amt": "caffein_daily_amt",
            "is_sadder": "is_sadder",
            "if_lost_interest": "if_lost_interest",
            "have_will": "have_will",
        }
        url = reverse('registration_models_update', args=[models.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


