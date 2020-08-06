from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
import uuid


class Labs(models.Model):
    # Fields
    slug = extension_fields.AutoSlugField(populate_from='lab_name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    lab_name = models.TextField(max_length=100, null=True, blank=True)
    lab_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    triage_id = models.CharField(max_length=100, null=True, blank=True)
    h01 = models.BooleanField(default=False)
    h02 = models.BooleanField(default=False)
    h03 = models.BooleanField(default=False)
    h04 = models.BooleanField(default=False)
    h05 = models.BooleanField(default=False)
    h06 = models.BooleanField(default=False)
    h07 = models.BooleanField(default=False)
    h08 = models.BooleanField(default=False)
    h09 = models.BooleanField(default=False)
    c01 = models.BooleanField(default=False)
    c02 = models.BooleanField(default=False)
    p01 = models.BooleanField(default=False)
    p02 = models.BooleanField(max_length=100, default=False)
    p03 = models.BooleanField(default=False)
    p04 = models.BooleanField(default=False)
    p05 = models.BooleanField(default=False)
    p06 = models.BooleanField(default=False)
    mbs01 = models.BooleanField(default=False)
    mbs02 = models.BooleanField(default=False)
    mbs03 = models.BooleanField(default=False)
    ge01 = models.BooleanField(default=False)
    lks01 = models.BooleanField(default=False)
    lks02 = models.BooleanField(default=False)
    lks03 = models.BooleanField(default=False)
    lks04 = models.BooleanField(default=False)
    lks05 = models.BooleanField(default=False)
    lks06 = models.BooleanField(default=False)
    lks07 = models.BooleanField(default=False)
    gm01 = models.BooleanField(default=False)
    gm02 = models.BooleanField(default=False)
    gm03 = models.BooleanField(default=False)
    lm01 = models.BooleanField(default=False)
    lm02 = models.BooleanField(default=False)
    lm03 = models.BooleanField(default=False)
    lm04 = models.BooleanField(default=False)
    lpg01 = models.BooleanField(default=False)
    lpg02 = models.BooleanField(default=False)
    lpg03 = models.BooleanField(max_length=100, default=False)
    lpg04 = models.BooleanField(default=False)
    lpg05 = models.BooleanField(default=False)
    lpg06 = models.BooleanField(default=False)
    lpg06 = models.BooleanField(default=False)
    lpg07 = models.BooleanField(default=False)
    lpg08 = models.BooleanField(default=False)
    hv01 = models.BooleanField(default=False)
    hv02 = models.BooleanField(default=False)
    hv03 = models.BooleanField(default=False)
    i01 = models.BooleanField(default=False)
    i02 = models.BooleanField(default=False)
    i03 = models.BooleanField(default=False)
    m01 = models.BooleanField(default=False)
    m02 = models.BooleanField(default=False)
    m03 = models.BooleanField(default=False)
    M04 = models.BooleanField(default=False)
    m05 = models.BooleanField(default=False)
    m06 = models.BooleanField(default=False)
    m07 = models.BooleanField(default=False)
    m08 = models.BooleanField(default=False)
    g01 = models.BooleanField(max_length=200, default=False)
    other = models.TextField(max_length=100, null=True, blank=True)
    diagnosis = models.TextField(max_length=100, null=True, blank=True)
    h01_alergy = models.BooleanField(default=False)
    h02_alergy = models.BooleanField(default=False)
    h03_alergy = models.BooleanField(default=False)
    h04_alergy = models.BooleanField(default=False)
    h06_alergy = models.BooleanField(default=False)
    h07_alergy = models.BooleanField(default=False)
    h08_alergy = models.BooleanField(max_length=100, default=False)
    c01_iron_studies = models.BooleanField(default=False)
    c01_cardiac_markers = models.BooleanField(max_length=100, default=False)
    c02_cardiac_markers = models.BooleanField(max_length=100, default=False)
    c02_cardiac_markers_1 = models.BooleanField(max_length=100, default=False)
    lks01_antenatal_screen = models.BooleanField(default=False)
    lks02_antenatal_screen = models.BooleanField(max_length=100, default=False)
    lks04_antenatal_screen = models.BooleanField(max_length=100, default=False)
    lks05_antenatal_screen = models.BooleanField(max_length=100, default=False)
    lks06_antenatal_screen = models.BooleanField(max_length=100, default=False)
    lks07_antenatal_screen = models.BooleanField(max_length=100, default=False)
    gm01_antenatal_screen = models.BooleanField(default=False)
    fsh_menopausal_screen = models.BooleanField(default=False)
    oestradiol_menopausal_screen = models.BooleanField(max_length=100, default=False)
    albumin_menopausal_screen = models.BooleanField(default=False)
    hv02_menopausal_screen = models.BooleanField(max_length=100, default=False)
    hv03_menopausal_screen = models.BooleanField(default=False)
    ast_menopausal_screen = models.BooleanField(max_length=100, default=False)
    i01_menopausal_screen = models.BooleanField(max_length=100, default=False)
    i02_menopausal_screen = models.BooleanField(default=False)
    i03_menopausal_screen = models.TextField(max_length=100, null=True, blank=True)
    patient_no = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('tests_labs_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('tests_labs_update', args=(self.slug,))


class Radiology(models.Model):
    # Fields
    slug = extension_fields.AutoSlugField(populate_from='patient_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    radiology_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    triage_id = models.CharField(max_length=100, null=True, blank=True)
    lpm_date = models.BooleanField(default=False)
    could_b_pregrant = models.TextField(max_length=100, null=True, blank=True)
    examination = models.TextField(max_length=200, null=True, blank=True)
    clinical_indication = models.TextField(max_length=200, null=True, blank=True)
    intra_orbital_fb_hist = models.BooleanField(default=False)
    intracranial_clip = models.BooleanField(default=False)
    pacemaker = models.BooleanField(default=False)
    cochlear_implants = models.BooleanField(default=False)
    prosthetic_hrt_valve = models.BooleanField(default=False)
    pregnancy = models.BooleanField(default=False)
    recent_surgery = models.BooleanField(default=False)
    patient_info = models.BooleanField(default=False)
    diabetic_metformin = models.BooleanField(default=False)
    allergic_contrast = models.BooleanField(default=False)
    other_allergies = models.BooleanField(max_length=100, default=False)
    kidney_problems = models.BooleanField(default=False)
    anticoagulant_drugs = models.BooleanField(default=False)
    egfr_result = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    patient_no = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('tests_radiology_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('tests_radiology_update', args=(self.slug,))


class RadiologyResult(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='patient_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    patient_no = models.CharField(max_length=30)
    results = models.TextField(max_length=400)
    radiologyresult_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    triage_id = models.CharField(max_length=255, null=True, blank=True)
    tests_done = models.TextField(max_length=400, null=True, blank=True)
    uploaded_file = models.FileField(upload_to='media/radiology/', null=True, blank=True)


    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('radiologyresult_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('radiologyresult_update', args=(self.slug,))


class LabResults(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='patient_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    labresult_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    triage_id = models.CharField(max_length=100, null=True, blank=True)
    patient_no = models.TextField(max_length=100)
    tests_done = models.TextField(max_length=400, null=True, blank=True)
    test_results = models.TextField(max_length=400)
    uploaded_file = models.FileField(upload_to='media/lab/', null=True, blank=True)


    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('labresults_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('labresults_update', args=(self.slug,))
