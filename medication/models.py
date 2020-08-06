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

class MyDawa(models.Model):
    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=300)
    price = models.CharField(max_length=300)

    class Meta:
        ordering = ('brand',)

    def __str__(self):
        return self.brand + " : " + self.size + ":" + self.price


class Medication(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='patient_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    prescription_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    triage_id = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=50, blank=True)
    patient_no = models.CharField(max_length=30)
    patient_name = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    physical_address = models.TextField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=30)
    signature = models.BinaryField(null=True, blank=True)
    prescription = models.TextField(max_length=400)



    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('medication_models_detail', args=(self.slug,))

    def get_update_url(self):
       return reverse('medication_models_update', args=(self.slug,))


