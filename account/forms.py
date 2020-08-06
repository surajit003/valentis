from django import forms
from .models import CustomUser


class LoginForm(forms.Form):
    email_address = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'mdl-textfield__input',
        'id': 'login'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'mdl-textfield__input',
        'type': 'password',
        'id': 'password'
    }))

class CustomUserForm(forms.ModelForm):

    # first_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'mdl-textfield__input',
    #     'type': 'text',
    #     'id': 'first_name'
    # }))
    #
    # phone_number = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'mdl-textfield__input',
    #     'type': 'text',
    #     'id': 'phone_number'
    # }))
    #
    # staff_number = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'mdl-textfield__input',
    #     'type': 'text',
    #     'id': 'staff_number'
    # }))
    #
    # id_number = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'mdl-textfield__input',
    #     'type': 'text',
    #     'id': 'id_number'
    # }))
    #
    # last_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'mdl-textfield__input',
    #     'type': 'text',
    #     'id': 'last_name'
    # }))
    #
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #     'class': 'mdl-textfield__input',
    #     'id': 'email'
    # }))
    #
    role = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'mdl-textfield__input',
        'type': 'text',
        'id': 'role'
    }))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'staff_number', 'id_number', 'email']


class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(max_length=40)
    new_password = forms.CharField(max_length=40)
