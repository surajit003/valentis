import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Labs, Radiology
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


def create_labs(**kwargs):
    defaults = {}
    defaults["lab_name"] = "lab_name"
    defaults["h01"] = "h01"
    defaults["h02"] = "h02"
    defaults["h03"] = "h03"
    defaults["h04"] = "h04"
    defaults["h05"] = "h05"
    defaults["h06"] = "h06"
    defaults["h07"] = "h07"
    defaults["h08"] = "h08"
    defaults["h09"] = "h09"
    defaults["c01"] = "c01"
    defaults["c02"] = "c02"
    defaults["p01"] = "p01"
    defaults["p02"] = "p02"
    defaults["p03"] = "p03"
    defaults["p04"] = "p04"
    defaults["p05"] = "p05"
    defaults["p06"] = "p06"
    defaults["mbs01"] = "mbs01"
    defaults["mbs02"] = "mbs02"
    defaults["mbs03"] = "mbs03"
    defaults["ge01"] = "ge01"
    defaults["lks01"] = "lks01"
    defaults["lks02"] = "lks02"
    defaults["lks03"] = "lks03"
    defaults["lks04"] = "lks04"
    defaults["lks05"] = "lks05"
    defaults["lks06"] = "lks06"
    defaults["lks07"] = "lks07"
    defaults["gm01"] = "gm01"
    defaults["gm02"] = "gm02"
    defaults["gm03"] = "gm03"
    defaults["lm01"] = "lm01"
    defaults["lm02"] = "lm02"
    defaults["lm03"] = "lm03"
    defaults["lm04"] = "lm04"
    defaults["lpg01"] = "lpg01"
    defaults["lpg02"] = "lpg02"
    defaults["lpg03"] = "lpg03"
    defaults["lpg04"] = "lpg04"
    defaults["lpg05"] = "lpg05"
    defaults["lpg06"] = "lpg06"
    defaults["lpg06"] = "lpg06"
    defaults["lpg07"] = "lpg07"
    defaults["lpg08"] = "lpg08"
    defaults["hv01"] = "hv01"
    defaults["hv02"] = "hv02"
    defaults["hv03"] = "hv03"
    defaults["i01"] = "i01"
    defaults["i02"] = "i02"
    defaults["i03"] = "i03"
    defaults["m01"] = "m01"
    defaults["m02"] = "m02"
    defaults["m03"] = "m03"
    defaults["M04"] = "M04"
    defaults["m05"] = "m05"
    defaults["m06"] = "m06"
    defaults["m07"] = "m07"
    defaults["m08"] = "m08"
    defaults["g01"] = "g01"
    defaults["other"] = "other"
    defaults["diagnosis"] = "diagnosis"
    defaults["h01_alergy"] = "h01_alergy"
    defaults["h02_alergy"] = "h02_alergy"
    defaults["h03_alergy"] = "h03_alergy"
    defaults["h04_alergy"] = "h04_alergy"
    defaults["h06_alergy"] = "h06_alergy"
    defaults["h07_alergy"] = "h07_alergy"
    defaults["h08_alergy"] = "h08_alergy"
    defaults["c01_iron_studies"] = "c01_iron_studies"
    defaults["c01_cardiac_markers"] = "c01_cardiac_markers"
    defaults["c02_cardiac_markers"] = "c02_cardiac_markers"
    defaults["c02_cardiac_markers_1"] = "c02_cardiac_markers_1"
    defaults["lks01_antenatal_screen"] = "lks01_antenatal_screen"
    defaults["lks02_antenatal_screen"] = "lks02_antenatal_screen"
    defaults["lks04_antenatal_screen"] = "lks04_antenatal_screen"
    defaults["lks05_antenatal_screen"] = "lks05_antenatal_screen"
    defaults["lks06_antenatal_screen"] = "lks06_antenatal_screen"
    defaults["lks07_antenatal_screen"] = "lks07_antenatal_screen"
    defaults["gm01_antenatal_screen"] = "gm01_antenatal_screen"
    defaults["fsh_menopausal_screen"] = "fsh_menopausal_screen"
    defaults["oestradiol_menopausal_screen"] = "oestradiol_menopausal_screen"
    defaults["albumin_menopausal_screen"] = "albumin_menopausal_screen"
    defaults["hv02_menopausal_screen"] = "hv02_menopausal_screen"
    defaults["hv03_menopausal_screen"] = "hv03_menopausal_screen"
    defaults["ast_menopausal_screen"] = "ast_menopausal_screen"
    defaults["i01_menopausal_screen"] = "i01_menopausal_screen"
    defaults["i02_menopausal_screen"] = "i02_menopausal_screen"
    defaults["i03_menopausal_screen"] = "i03_menopausal_screen"
    defaults["patient_no"] = "patient_no"
    defaults.update(**kwargs)
    return Labs.objects.create(**defaults)


def create_radiology(**kwargs):
    defaults = {}
    defaults["lpm_date"] = "lpm_date"
    defaults["could_b_pregrant"] = "could_b_pregrant"
    defaults["examination"] = "examination"
    defaults["clinical_indication"] = "clinical_indication"
    defaults["intra_orbital_fb_hist"] = "intra_orbital_fb_hist"
    defaults["intracranial_clip"] = "intracranial_clip"
    defaults["pacemaker"] = "pacemaker"
    defaults["cochlear_implants"] = "cochlear_implants"
    defaults["prosthetic_hrt_valve"] = "prosthetic_hrt_valve"
    defaults["pregnancy"] = "pregnancy"
    defaults["recent_surgery"] = "recent_surgery"
    defaults["patient_info"] = "patient_info"
    defaults["diabetic_metformin"] = "diabetic_metformin"
    defaults["allergic_contrast"] = "allergic_contrast"
    defaults["other_allergies"] = "other_allergies"
    defaults["kidney_problems"] = "kidney_problems"
    defaults["anticoagulant_drugs"] = "anticoagulant_drugs"
    defaults["egfr_result"] = "egfr_result"
    defaults["date"] = "date"
    defaults["patient_no"] = "patient_no"
    defaults.update(**kwargs)
    return Radiology.objects.create(**defaults)


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


def create_radiologyresult(**kwargs):
    defaults = {}
    defaults["patient_no"] = "patient_no"
    defaults["results"] = "results"
    defaults["tests_done"] = "tests_done"
    defaults.update(**kwargs)
    return RadiologyResult.objects.create(**defaults)


def create_labresults(**kwargs):
    defaults = {}
    defaults["patient_no"] = "patient_no"
    defaults["tests_done"] = "tests_done"
    defaults["test_results"] = "test_results"
    defaults.update(**kwargs)
    return LabResults.objects.create(**defaults)


class RadiologyResultViewTest(unittest.TestCase):
    '''
    Tests for RadiologyResult
    '''
    def setUp(self):
        self.client = Client()

    def test_list_radiologyresult(self):
        url = reverse('radiology_radiologyresult_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_radiologyresult(self):
        url = reverse('radiology_radiologyresult_create')
        data = {
            "patient_no": "patient_no",
            "results": "results",
            "tests_done": "tests_done",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_radiologyresult(self):
        radiologyresult = create_radiologyresult()
        url = reverse('radiology_radiologyresult_detail', args=[radiologyresult.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_radiologyresult(self):
        radiologyresult = create_radiologyresult()
        data = {
            "patient_no": "patient_no",
            "results": "results",
            "tests_done": "tests_done",
        }
        url = reverse('radiology_radiologyresult_update', args=[radiologyresult.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class labsViewTest(unittest.TestCase):
    '''
    Tests for tests
    '''
    def setUp(self):
        self.client = Client()

    def test_list_labs(self):
        url = reverse('labs_labs_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_labs(self):
        url = reverse('labs_labs_create')
        data = {
            "lab_name": "lab_name",
            "h01": "h01",
            "h02": "h02",
            "h03": "h03",
            "h04": "h04",
            "h05": "h05",
            "h06": "h06",
            "h07": "h07",
            "h08": "h08",
            "h09": "h09",
            "c01": "c01",
            "c02": "c02",
            "p01": "p01",
            "p02": "p02",
            "p03": "p03",
            "p04": "p04",
            "p05": "p05",
            "p06": "p06",
            "mbs01": "mbs01",
            "mbs02": "mbs02",
            "mbs03": "mbs03",
            "ge01": "ge01",
            "lks01": "lks01",
            "lks02": "lks02",
            "lks03": "lks03",
            "lks04": "lks04",
            "lks05": "lks05",
            "lks06": "lks06",
            "lks07": "lks07",
            "gm01": "gm01",
            "gm02": "gm02",
            "gm03": "gm03",
            "lm01": "lm01",
            "lm02": "lm02",
            "lm03": "lm03",
            "lm04": "lm04",
            "lpg01": "lpg01",
            "lpg02": "lpg02",
            "lpg03": "lpg03",
            "lpg04": "lpg04",
            "lpg05": "lpg05",
            "lpg06": "lpg06",
            "lpg06": "lpg06",
            "lpg07": "lpg07",
            "lpg08": "lpg08",
            "hv01": "hv01",
            "hv02": "hv02",
            "hv03": "hv03",
            "i01": "i01",
            "i02": "i02",
            "i03": "i03",
            "m01": "m01",
            "m02": "m02",
            "m03": "m03",
            "M04": "M04",
            "m05": "m05",
            "m06": "m06",
            "m07": "m07",
            "m08": "m08",
            "g01": "g01",
            "other": "other",
            "diagnosis": "diagnosis",
            "h01_alergy": "h01_alergy",
            "h02_alergy": "h02_alergy",
            "h03_alergy": "h03_alergy",
            "h04_alergy": "h04_alergy",
            "h06_alergy": "h06_alergy",
            "h07_alergy": "h07_alergy",
            "h08_alergy": "h08_alergy",
            "c01_iron_studies": "c01_iron_studies",
            "c01_cardiac_markers": "c01_cardiac_markers",
            "c02_cardiac_markers": "c02_cardiac_markers",
            "c02_cardiac_markers_1": "c02_cardiac_markers_1",
            "lks01_antenatal_screen": "lks01_antenatal_screen",
            "lks02_antenatal_screen": "lks02_antenatal_screen",
            "lks04_antenatal_screen": "lks04_antenatal_screen",
            "lks05_antenatal_screen": "lks05_antenatal_screen",
            "lks06_antenatal_screen": "lks06_antenatal_screen",
            "lks07_antenatal_screen": "lks07_antenatal_screen",
            "gm01_antenatal_screen": "gm01_antenatal_screen",
            "fsh_menopausal_screen": "fsh_menopausal_screen",
            "oestradiol_menopausal_screen": "oestradiol_menopausal_screen",
            "albumin_menopausal_screen": "albumin_menopausal_screen",
            "hv02_menopausal_screen": "hv02_menopausal_screen",
            "hv03_menopausal_screen": "hv03_menopausal_screen",
            "ast_menopausal_screen": "ast_menopausal_screen",
            "i01_menopausal_screen": "i01_menopausal_screen",
            "i02_menopausal_screen": "i02_menopausal_screen",
            "i03_menopausal_screen": "i03_menopausal_screen",
            "patient_no": "patient_no",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_labs(self):
        labs = create_labs()
        url = reverse('labs_labs_detail', args=[labs.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_labs(self):
        labs = create_labs()
        data = {
            "lab_name": "lab_name",
            "h01": "h01",
            "h02": "h02",
            "h03": "h03",
            "h04": "h04",
            "h05": "h05",
            "h06": "h06",
            "h07": "h07",
            "h08": "h08",
            "h09": "h09",
            "c01": "c01",
            "c02": "c02",
            "p01": "p01",
            "p02": "p02",
            "p03": "p03",
            "p04": "p04",
            "p05": "p05",
            "p06": "p06",
            "mbs01": "mbs01",
            "mbs02": "mbs02",
            "mbs03": "mbs03",
            "ge01": "ge01",
            "lks01": "lks01",
            "lks02": "lks02",
            "lks03": "lks03",
            "lks04": "lks04",
            "lks05": "lks05",
            "lks06": "lks06",
            "lks07": "lks07",
            "gm01": "gm01",
            "gm02": "gm02",
            "gm03": "gm03",
            "lm01": "lm01",
            "lm02": "lm02",
            "lm03": "lm03",
            "lm04": "lm04",
            "lpg01": "lpg01",
            "lpg02": "lpg02",
            "lpg03": "lpg03",
            "lpg04": "lpg04",
            "lpg05": "lpg05",
            "lpg06": "lpg06",
            "lpg06": "lpg06",
            "lpg07": "lpg07",
            "lpg08": "lpg08",
            "hv01": "hv01",
            "hv02": "hv02",
            "hv03": "hv03",
            "i01": "i01",
            "i02": "i02",
            "i03": "i03",
            "m01": "m01",
            "m02": "m02",
            "m03": "m03",
            "M04": "M04",
            "m05": "m05",
            "m06": "m06",
            "m07": "m07",
            "m08": "m08",
            "g01": "g01",
            "other": "other",
            "diagnosis": "diagnosis",
            "h01_alergy": "h01_alergy",
            "h02_alergy": "h02_alergy",
            "h03_alergy": "h03_alergy",
            "h04_alergy": "h04_alergy",
            "h06_alergy": "h06_alergy",
            "h07_alergy": "h07_alergy",
            "h08_alergy": "h08_alergy",
            "c01_iron_studies": "c01_iron_studies",
            "c01_cardiac_markers": "c01_cardiac_markers",
            "c02_cardiac_markers": "c02_cardiac_markers",
            "c02_cardiac_markers_1": "c02_cardiac_markers_1",
            "lks01_antenatal_screen": "lks01_antenatal_screen",
            "lks02_antenatal_screen": "lks02_antenatal_screen",
            "lks04_antenatal_screen": "lks04_antenatal_screen",
            "lks05_antenatal_screen": "lks05_antenatal_screen",
            "lks06_antenatal_screen": "lks06_antenatal_screen",
            "lks07_antenatal_screen": "lks07_antenatal_screen",
            "gm01_antenatal_screen": "gm01_antenatal_screen",
            "fsh_menopausal_screen": "fsh_menopausal_screen",
            "oestradiol_menopausal_screen": "oestradiol_menopausal_screen",
            "albumin_menopausal_screen": "albumin_menopausal_screen",
            "hv02_menopausal_screen": "hv02_menopausal_screen",
            "hv03_menopausal_screen": "hv03_menopausal_screen",
            "ast_menopausal_screen": "ast_menopausal_screen",
            "i01_menopausal_screen": "i01_menopausal_screen",
            "i02_menopausal_screen": "i02_menopausal_screen",
            "i03_menopausal_screen": "i03_menopausal_screen",
            "patient_no": "patient_no",
        }
        url = reverse('labs_labs_update', args=[labs.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class radiologyViewTest(unittest.TestCase):
    '''
    Tests for radiology
    '''
    def setUp(self):
        self.client = Client()

    def test_list_radiology(self):
        url = reverse('tests_radiology_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_radiology(self):
        url = reverse('labs_radiology_create')
        data = {
            "lpm_date": "lpm_date",
            "could_b_pregrant": "could_b_pregrant",
            "examination": "examination",
            "clinical_indication": "clinical_indication",
            "intra_orbital_fb_hist": "intra_orbital_fb_hist",
            "intracranial_clip": "intracranial_clip",
            "pacemaker": "pacemaker",
            "cochlear_implants": "cochlear_implants",
            "prosthetic_hrt_valve": "prosthetic_hrt_valve",
            "pregnancy": "pregnancy",
            "recent_surgery": "recent_surgery",
            "patient_info": "patient_info",
            "diabetic_metformin": "diabetic_metformin",
            "allergic_contrast": "allergic_contrast",
            "other_allergies": "other_allergies",
            "kidney_problems": "kidney_problems",
            "anticoagulant_drugs": "anticoagulant_drugs",
            "egfr_result": "egfr_result",
            "date": "date",
            "patient_no": "patient_no",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_radiology(self):
        radiology = create_radiology()
        url = reverse('labs_radiology_detail', args=[radiology.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_radiology(self):
        radiology = create_radiology()
        data = {
            "lpm_date": "lpm_date",
            "could_b_pregrant": "could_b_pregrant",
            "examination": "examination",
            "clinical_indication": "clinical_indication",
            "intra_orbital_fb_hist": "intra_orbital_fb_hist",
            "intracranial_clip": "intracranial_clip",
            "pacemaker": "pacemaker",
            "cochlear_implants": "cochlear_implants",
            "prosthetic_hrt_valve": "prosthetic_hrt_valve",
            "pregnancy": "pregnancy",
            "recent_surgery": "recent_surgery",
            "patient_info": "patient_info",
            "diabetic_metformin": "diabetic_metformin",
            "allergic_contrast": "allergic_contrast",
            "other_allergies": "other_allergies",
            "kidney_problems": "kidney_problems",
            "anticoagulant_drugs": "anticoagulant_drugs",
            "egfr_result": "egfr_result",
            "date": "date",
            "patient_no": "patient_no",
        }
        url = reverse('labs_radiology_update', args=[radiology.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



class LabResultsViewTest(unittest.TestCase):
    '''
    Tests for LabResults
    '''
    def setUp(self):
        self.client = Client()

    def test_list_labresults(self):
        url = reverse('radiology_labresults_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_labresults(self):
        url = reverse('radiology_labresults_create')
        data = {
            "patient_no": "patient_no",
            "tests_done": "tests_done",
            "test_results": "test_results",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_labresults(self):
        labresults = create_labresults()
        url = reverse('radiology_labresults_detail', args=[labresults.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_labresults(self):
        labresults = create_labresults()
        data = {
            "patient_no": "patient_no",
            "tests_done": "tests_done",
            "test_results": "test_results",
        }
        url = reverse('radiology_labresults_update', args=[labresults.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


