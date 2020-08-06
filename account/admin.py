from django.contrib import admin
from django import forms
from .models import CustomUser, CustomUserManager, EmailLog

class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserAdminForm
    list_display = ['email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'is_active', 'id_number', 'staff_number','activation_key', 'activation_key_expires', 'account_verified_date', 'verification_code']

admin.site.register(CustomUser, CustomUserAdmin)


class EmailTemplateAdminForm(forms.ModelForm):
    class Meta:
        model = EmailLog
        fields = '__all__'


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['template_key', 'subject', 'from_email', 'to_email']
    save_as = True

admin.site.register(EmailLog, EmailTemplateAdmin)