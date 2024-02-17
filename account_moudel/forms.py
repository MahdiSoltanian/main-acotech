from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    phone_number = forms.IntegerField(
        label='phone_number',

    )

    name = forms.CharField(
        label='name'
    )

    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput()
    )

    confirm_password = forms.CharField(
        label='confirm password',
        widget=forms.PasswordInput()
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('notmach')


class LoginForm(forms.Form):
    phone_number = forms.IntegerField(
        label='phone_number',
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput()
    )
