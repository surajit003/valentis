from . import models

from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Patient
        fields = (
            'pk',
            'user',
            'patient_no', 
            'created', 
            'last_updated', 
            'first_name', 
            'middle_name', 
            'last_name', 
            'gender', 
            'street_name', 
            'apartment_name', 
            'postal_code', 
            'postal_address', 
            'city', 
            'country', 
            'age', 
            'next_of_kin', 
            'n_of_kin_rel', 
            'email', 
            'phone', 
            'primary_insurance', 
            'secondary_insurance', 
            'pri_ins_sub', 
            'sec_ins_sub', 
            'other_ins_subscriber', 
            'subscriber_relationship', 
            'sub_address', 
            'ss_number', 
            'sub_ss_number', 
            'alt_phone', 
            'sub_work_phone', 
            'dob', 
            'sub_dob', 
            'sub_employer',

            'occupation',
            'marital_status',
            'spouse',
            'no_children',
            'childrens',
            'prev_docs',
            'medical_information',
            'alergies',
            'preferred_pharmacy',
            'last_phys_examination',
            'last_blood_work',
            'last_colonoscopy',
            'last_tetanus_shot',
            'last_menstrual',
            'last_pap_smear',
            'last_mammogram',
            'dexa',
            'no_pregnancies',
            'miscourages',
            'living_children',
            'methods_of_contraception',
            'surgeries',
            'genetic_diseases',
            'if_smoker',
            'cigar_per_day',
            'no_of_yr_smoking',
            'if_chew_tobacco',
            'yrs_chewing_tobacco',
            'if_quit_before',
            'tobacco_quit_duration',
            'if_drink_alcohol',
            'alocohol_type',
            'alcohol_frequency',
            'if_drug_used',
            'drug_type',
            'when_drug_used',
            'if_exercise',
            'exercise_freq',
            'if_special_diet',
            'special_diet',
            'if_use_caffein',
            'caffein_daily_amt',
            'is_sadder',
            'if_lost_interest',
            'have_will',
            'uploaded_file',
            'social_hist', 'fam_hist',
        )



class allergiesserializer(serializers.ModelSerializer):

    class Meta:
        model = models.Allergies
        fields = (
           'allergy_name',


        )
class countyserializer(serializers.ModelSerializer):

    class Meta:
        model = models.County
        fields = (
           'County',


        )

class medicationserializer(serializers.ModelSerializer):

    class Meta:
        model = models.MedicationHistory
        fields = (
           'Disease',


        )
class insuranceserializer(serializers.ModelSerializer):

    class Meta:
        model = models.InsuranceCompanies
        fields = (
           'Name',


        )

