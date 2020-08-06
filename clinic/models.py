from django.core.urlresolvers import reverse
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

class PatientVisit(models.Model):

    # Fields
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = extension_fields.AutoSlugField(populate_from='patient_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    patient_no = models.CharField(max_length=30, null=True, blank=True)
    visit_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radiology_no = models.CharField(max_length=255, null=True, blank=True)
    triage_id = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(max_length=200, null=True, blank=True)
    diagnosis = models.TextField(max_length=100, null=True, blank=True)
    prescription_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    examination = models.CharField(max_length=255, null=True, blank=True)
    plan_of_managemnt = models.CharField(max_length=255, null=True, blank=True)
    query_diagnosis = models.CharField(max_length=255, null=True, blank=True)
    his_presenting_illness = models.CharField(max_length=255, null=True, blank=True)
    attending_doctor = models.CharField(max_length=255, null=True, blank=True)
    diag_search = models.CharField(max_length=255, null=True, blank=True)



    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('clinic_patientvisit_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('clinic_patientvisit_update', args=(self.slug,))

class Diagnosis(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=500)

class Radiologylist(models.Model):
    group = models.CharField(max_length=255,blank=True)
    modality = models.CharField(max_length=255,blank=True)
    tests = models.CharField(max_length=300,blank=True)
