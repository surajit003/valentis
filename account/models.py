from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string, get_template
from .tokens import account_activation_token
from django.contrib.auth import login
import datetime

from django import template
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.db import models
from django.template import Context


class EmailLog(models.Model):
    """
    Email templates get stored in database so that admins can
    change emails on the fly
    """
    subject = models.CharField(max_length=255, blank=True, null=True)
    to_email = models.CharField(max_length=255, blank=True, null=True)
    from_email = models.CharField(max_length=255, blank=True, null=True)
    html_template = models.TextField(blank=True, null=True)
    plain_text = models.TextField(blank=True, null=True)
    is_html = models.BooleanField(default=False)
    is_text = models.BooleanField(default=False)

    # unique identifier of the email template
    template_key = models.CharField(max_length=255, unique=True)

    def get_rendered_template(self, tpl, context):
        return self.get_template(tpl).render(context)

    def get_template(self, tpl):
        return template.Template(tpl)

    def get_subject(self, subject, context):
        return subject or self.get_rendered_template(self.subject, context)

    def get_body(self, body, context):
        return body or self.get_rendered_template(self._get_body(), context)

    def get_sender(self):
        return self.from_email or settings.DEFAULT_FROM_EMAIL

    def get_recipient(self, emails, context):
        return emails or [self.get_rendered_template(self.to_email, context)]

    @staticmethod
    def send(*args, **kwargs):
        EmailLog._send(*args, **kwargs)

    @staticmethod
    def _send(template_key, context, subject=None, body=None, sender=None,
              emails=None, bcc=None, attachments=None):
        mail_template = EmailLog.objects.get(template_key=template_key)
        context = Context(context)

        subject = mail_template.get_subject(subject, context)
        body = mail_template.get_body(body, context)
        sender = sender or mail_template.get_sender()
        emails = mail_template.get_recipient(emails, context)

        if mail_template.is_text:
            return send_mail(subject, body, sender, emails, fail_silently=not
            settings.DEBUG)

        msg = EmailMultiAlternatives(subject, body, sender, emails,
                                     alternatives=((body, 'text/html'),),
                                     bcc=bcc
                                     )
        if attachments:
            for name, content, mimetype in attachments:
                msg.attach(name, content, mimetype)
        return msg.send(fail_silently=not (settings.DEBUG or settings.TEST))

    def _get_body(self):
        if self.is_text:
            return self.plain_text

        return self.html_template

    def __str__(self):
        return "<{}> {}".format(self.template_key, self.subject)


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(
        _('first name'), max_length=30, null=True)
    last_name = models.CharField(
        _('last name'), max_length=30, null=True)
    phone_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9]{9,15}$', message="Enter a valid phone number (9 - 15 digits).")
    phone_number = models.CharField(
        _('phone number'), max_length=30, null=True, validators=[phone_regex])
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=False,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    id_number = models.CharField(
        _('id number'), max_length=20, unique=True, null=True)
    staff_number = models.CharField(
        _('staff number'), max_length=30, unique=True, null=True)
    activation_key = models.CharField(max_length=40, blank=True, null=True)
    activation_key_expires = models.DateTimeField(blank=True, null=True)
    verification_code = models.IntegerField(blank=True, null=True)
    verification_code_expires = models.DateTimeField(blank=True, null=True)
    account_verified_date = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_seen = models.DateTimeField(_('last seen'), blank=True, null=True)
    force_logout_date = models.DateTimeField(null=True)
    is_patient = models.BooleanField(default=False,
                                     help_text=_('Designates whether the user can log into the website.'))

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['id']
        default_permissions = ()
        permissions = (
            ('create_deactivate_user', 'Accounts - Can add/deactivate a user'),
            ('edit_user', 'Accounts - Can edit details of a user'),
        )

    def __unicode__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('system-user', kwargs={'pk': self.pk})

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def user_site(self):
        if self.is_site_user:
            try:
                site = self.site_user.get(is_active=True)
                return site.site
            except ObjectDoesNotExist:
                pass
        return None

    def random_password(self, length=10,
                        allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                      'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                      '23456789'):

        """
        Generate a random password with the given length and given
        allowed_chars. The default value of allowed_chars does not have "I" or
        "O" or letters and digits that look similar -- just to avoid confusion.
        """
        return get_random_string(length, allowed_chars)

    def send_confirmation(self, request):
        current_site = get_current_site(request)
        mail_subject = 'Activate your ValentisHealth clinic account.'
        token = account_activation_token.make_token(self)

        self.activation_key = token
        self.activation_key_expires = self.one_day_hence()
        self.save()

        d = {
            'user': self,
            'domain': current_site.domain,
            'email': self.email,
            'token': token,
        }

        msg_plain = render_to_string('activate_email.txt', d)
        msg_html = render_to_string('activate_email.html', d)

        send_mail(
            mail_subject,
            msg_plain,
            'notifications@valentis.co.ke',
            [self.email],
            html_message=msg_html,
        )

    def activate(self, request):
        if self.activation_past_due():
            self.is_active = True
            self.account_verified_date = datetime.datetime.now()
            self.save()

            login(request, self)
            # return redirect('home')
            password = self.random_password()
            self.set_password(password)
            message = "Your password is: \n" + password + "\nYour username is: " + self.email
            self.email_user("Your Valentis Health Clinic System Password", message, from_email=None)
            print(password)
            # user.is_active = True
            self.save()

            return {'status':True, 'message': 'succesful'}
        else:
            return {'status':False, 'message': 'Link expired'}


    def one_day_hence(self):
        return timezone.now() + timezone.timedelta(days=1)

    def activation_past_due(self):
        return self.activation_key_expires.replace(tzinfo=None) > datetime.datetime.now()
