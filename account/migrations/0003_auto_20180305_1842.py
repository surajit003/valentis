# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 15:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180305_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number (9 - 15 digits).', regex='^[a-zA-Z0-9]{9,15}$')], verbose_name='phone number'),
        ),
    ]
