from django.contrib import admin
from django import forms
from .models import member_info, member_benefits, member_anniversary, member_acceptance, principal_applicant, pre_authorization, provider, cash

class member_infoAdminForm(forms.ModelForm):

    class Meta:
        model = member_info
        fields = '__all__'


class member_infoAdmin(admin.ModelAdmin):
    form = member_infoAdminForm
    list_display = ['family_no','member_no', 'surname', 'first_name', 'other_name', 'dob', 'user_id', 'date_entered', 'cancelled', 'employment_no', 'gender', 'passport_no']
    # readonly_fields = ['family_no', 'created', 'last_updated', 'member_no', 'surname', 'first_name', 'other_name', 'dob', 'user_id', 'date_entered', 'cancelled', 'employment_no', 'gender', 'passport_no']

admin.site.register(member_info, member_infoAdmin)


class member_benefitsAdminForm(forms.ModelForm):

    class Meta:
        model = member_benefits
        fields = '__all__'


class member_benefitsAdmin(admin.ModelAdmin):
    form = member_benefitsAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'member_no', 'limit', 'sharing', 'anniv', 'suspended', 'expense', 'idx', 'balance']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'member_no', 'limit', 'sharing', 'anniv', 'suspended', 'expense', 'idx', 'balance']

admin.site.register(member_benefits, member_benefitsAdmin)


class member_anniversaryAdminForm(forms.ModelForm):

    class Meta:
        model = member_anniversary
        fields = '__all__'


class member_anniversaryAdmin(admin.ModelAdmin):
    form = member_anniversaryAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'member_no', 'start_date', 'end_date', 'anniv']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'member_no', 'start_date', 'end_date', 'anniv']

admin.site.register(member_anniversary, member_anniversaryAdmin)


class member_acceptanceAdminForm(forms.ModelForm):

    class Meta:
        model = member_acceptance
        fields = '__all__'


class member_acceptanceAdmin(admin.ModelAdmin):
    form = member_acceptanceAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'member_no', 'status', 'status_date', 'user_id', 'date_entered']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'member_no', 'status', 'status_date', 'user_id', 'date_entered']

admin.site.register(member_acceptance, member_acceptanceAdmin)


class principal_applicantAdminForm(forms.ModelForm):

    class Meta:
        model = principal_applicant
        fields = '__all__'


class principal_applicantAdmin(admin.ModelAdmin):
    form = principal_applicantAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'family_no', 'first_name', 'postal_add', 'town', 'email', 'other_names', 'corp_id', 'mobile_no', 'family_size', 'user_id', 'category']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'family_no', 'first_name', 'postal_add', 'town', 'email', 'other_names', 'corp_id', 'mobile_no', 'family_size', 'user_id', 'category']

admin.site.register(principal_applicant, principal_applicantAdmin)


class pre_authorizationAdminForm(forms.ModelForm):

    class Meta:
        model = pre_authorization
        fields = '__all__'


class pre_authorizationAdmin(admin.ModelAdmin):
    form = pre_authorizationAdminForm
    list_display = ['name', 'created', 'last_updated', 'member_no', 'provider', 'date_reported', 'reported_by', 'authorized_by', 'date_authorized', 'pre_diagnosis', 'authority_type', 'ward', 'available_limit', 'admit_days', 'reserve', 'notes', 'anniv', 'day_bed_charge', 'date_admitted', 'code']
    # readonly_fields = ['name', 'created', 'last_updated', 'member_no', 'provider', 'date_reported', 'reported_by', 'authorized_by', 'date_authorized', 'pre_diagnosis', 'authority_type', 'ward', 'available_limit', 'admit_days', 'reserve', 'notes', 'anniv', 'day_bed_charge', 'date_admitted', 'code']

admin.site.register(pre_authorization, pre_authorizationAdmin)


class providerAdminForm(forms.ModelForm):

    class Meta:
        model = provider
        fields = '__all__'


class providerAdmin(admin.ModelAdmin):
    form = providerAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'code', 'provider']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'code', 'provider']

admin.site.register(provider, providerAdmin)


class cashAdminForm(forms.ModelForm):

    class Meta:
        model = cash
        fields = '__all__'


class cashAdmin(admin.ModelAdmin):
    form = cashAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'items', 'amount_payed', 'total_cost', 'balance']
        # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'items', 'amount_payed', 'total_cost', 'balance']

admin.site.register(cash, cashAdmin)


