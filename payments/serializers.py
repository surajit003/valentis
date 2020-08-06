from . import models

from rest_framework import serializers


class member_infoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.member_info
        fields = (
            'slug',
            'family_no',
            'member_no',
            'surname', 
            'first_name', 
            'other_name', 
            'dob', 
            'user_id', 
            'date_entered', 
            'cancelled', 
            'employment_no', 
            'gender', 
            'passport_no', 
        )


class member_benefitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.member_benefits
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'member_no', 
            'limit', 
            'sharing', 
            'anniv', 
            'suspended', 
            'expense', 
            'idx', 
            'balance', 
        )


class member_anniversarySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.member_anniversary
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'member_no', 
            'start_date', 
            'end_date', 
            'anniv', 
        )


class member_acceptanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.member_acceptance
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'member_no', 
            'status', 
            'status_date', 
            'user_id', 
            'date_entered', 
        )


class principal_applicantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.principal_applicant
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'family_no', 
            'first_name', 
            'postal_add', 
            'town', 
            'email', 
            'other_names', 
            'corp_id', 
            'mobile_no', 
            'family_size', 
            'user_id', 
            'category', 
        )


class pre_authorizationSerializer(serializers.ModelSerializer):
    # reserve = serializers.SerializerMethodField()
    #
    # def get_speed(self, obj):
    #     if obj.speed == 0:
    #         return "slow"
    #     else:
    #         return "fast"

    class Meta:
        model = models.pre_authorization
        fields = (
            'slug',
            'name',
            'created',
            'last_updated',
            'member_no',
            'provider',
            'date_reported',
            'reported_by',
            'authorized_by',
            'date_authorized',
            'pre_diagnosis',
            'authority_type',
            'ward',
            'available_limit',
            'admit_days',
            'reserve',
            'notes',
            'anniv',
            # 'auth_batch_no',
            'day_bed_charge',
            'date_admitted',
            'code',
        )


class providerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.provider
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'code', 
            'provider', 
        )


class cashSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.cash
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'items', 
            'amount_payed', 
            'total_cost', 
            'balance', 
        )


class memberinfosanlamserializer(serializers.ModelSerializer):
    class Meta:
        model = models.memberinfosanlamdatabase
        fields = (
            'FAMILY_NO',
            'MEMBER_NO',
            'FIRST_NAME',
            'SURNAME',
            'OTHER_NAMES',
            'DOB',
            'USER_ID',
            'CANCELLED',


        )


