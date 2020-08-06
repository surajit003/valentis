# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Allergy',
                'verbose_name_plural': 'Allergies',
            },
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('age', models.CharField(blank=True, default='NO', max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'child',
                'verbose_name_plural': 'children',
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('County', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceCompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('age', models.CharField(blank=True, default='NO', max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'child',
                'verbose_name_plural': 'children',
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='MedicationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Disease', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_no', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('street_name', models.CharField(blank=True, max_length=30, null=True)),
                ('apartment_name', models.CharField(blank=True, max_length=30, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=30, null=True)),
                ('postal_address', models.TextField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('next_of_kin', models.TextField(blank=True, max_length=100, null=True)),
                ('n_of_kin_rel', models.TextField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('primary_insurance', models.TextField(blank=True, max_length=10, null=True)),
                ('secondary_insurance', models.TextField(blank=True, max_length=100, null=True)),
                ('pri_ins_sub', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('sec_ins_sub', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('other_ins_subscriber', models.TextField(blank=True, max_length=100, null=True)),
                ('subscriber_relationship', models.TextField(blank=True, max_length=100, null=True)),
                ('sub_address', models.TextField(blank=True, max_length=100, null=True)),
                ('ss_number', models.TextField(blank=True, max_length=100, null=True)),
                ('sub_ss_number', models.TextField(blank=True, max_length=100, null=True)),
                ('alt_phone', models.IntegerField(blank=True, null=True)),
                ('sub_work_phone', models.TextField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('sub_dob', models.DateField(blank=True, null=True)),
                ('sub_employer', models.TextField(blank=True, max_length=100, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('session_id', models.TextField(blank=True, max_length=400, null=True)),
                ('uploaded_file', models.FileField(blank=True, null=True, upload_to='media/users/')),
                ('occupation', models.CharField(blank=True, default='None', max_length=30, null=True)),
                ('marital_status', models.CharField(blank=True, default='Single', max_length=30, null=True)),
                ('spouse', models.CharField(blank=True, max_length=30, null=True)),
                ('no_children', models.IntegerField(blank=True, null=True)),
                ('childrens', models.CharField(blank=True, max_length=100, null=True)),
                ('prev_docs', models.CharField(blank=True, max_length=200, null=True)),
                ('medical_information', models.TextField(blank=True, max_length=1000, null=True)),
                ('alergies', models.TextField(blank=True, max_length=1000, null=True)),
                ('preferred_pharmacy', models.TextField(blank=True, max_length=100, null=True)),
                ('last_phys_examination', models.DateField(blank=True, null=True)),
                ('last_blood_work', models.DateField(blank=True, null=True)),
                ('last_colonoscopy', models.DateField(blank=True, null=True)),
                ('last_tetanus_shot', models.DateField(blank=True, null=True)),
                ('last_menstrual', models.DateField(blank=True, null=True)),
                ('last_pap_smear', models.DateField(blank=True, null=True)),
                ('last_mammogram', models.DateField(blank=True, null=True)),
                ('dexa', models.TextField(blank=True, max_length=100, null=True)),
                ('no_pregnancies', models.IntegerField(blank=True, null=True)),
                ('miscourages', models.TextField(blank=True, max_length=100, null=True)),
                ('living_children', models.CharField(blank=True, max_length=30, null=True)),
                ('methods_of_contraception', models.TextField(blank=True, max_length=100, null=True)),
                ('surgeries', models.TextField(blank=True, max_length=1000, null=True)),
                ('genetic_diseases', models.TextField(blank=True, max_length=1000, null=True)),
                ('if_smoker', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('cigar_per_day', models.CharField(blank=True, max_length=30, null=True)),
                ('no_of_yr_smoking', models.CharField(blank=True, max_length=30, null=True)),
                ('if_chew_tobacco', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('yrs_chewing_tobacco', models.CharField(blank=True, max_length=30, null=True)),
                ('if_quit_before', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('tobacco_quit_duration', models.CharField(blank=True, max_length=30, null=True)),
                ('if_drink_alcohol', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('alocohol_type', models.CharField(blank=True, max_length=30, null=True)),
                ('alcohol_frequency', models.CharField(blank=True, max_length=30, null=True)),
                ('if_drug_used', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('drug_type', models.TextField(blank=True, max_length=100, null=True)),
                ('when_drug_used', models.CharField(blank=True, max_length=30, null=True)),
                ('if_exercise', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('exercise_freq', models.CharField(blank=True, max_length=30, null=True)),
                ('if_special_diet', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('special_diet', models.TextField(blank=True, max_length=100, null=True)),
                ('if_use_caffein', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('caffein_daily_amt', models.CharField(blank=True, max_length=30, null=True)),
                ('is_sadder', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('if_lost_interest', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('have_will', models.CharField(blank=True, default='NO', max_length=30, null=True)),
                ('social_hist', models.TextField(blank=True, max_length=400, null=True)),
                ('fam_hist', models.TextField(blank=True, max_length=400, null=True)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('patient_no', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.AddField(
            model_name='medication',
            name='patient_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication', to='registration.Patient', verbose_name='patient_no'),
        ),
        migrations.AddField(
            model_name='children',
            name='patient_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='registration.Patient', verbose_name='patient_no'),
        ),
    ]