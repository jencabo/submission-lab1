# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from statistics import mode
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import TenantUser


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    address = forms.CharField(required=False, max_length=255)
    city = forms.CharField(required=False, max_length=100)
    country = forms.CharField(required=False, max_length=100)
    postal_code = forms.CharField(required=False, max_length=20)
    about_me = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        self.tenantuser = kwargs.pop('tenantuser', None)
        super().__init__(*args, **kwargs)

        print(self.tenantuser)

        if self.tenantuser:
            self.fields['address'].initial = self.tenantuser.address
            self.fields['city'].initial = self.tenantuser.city
            self.fields['country'].initial = self.tenantuser.country
            #self.fields['postalcode'].initial = self.tenantuser.postalcode
            self.fields['aboutme'].initial = self.tenantuser.aboutme

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        if self.tenantuser:
            self.tenantuser.address = self.cleaned_data['address']
            self.tenantuser.city = self.cleaned_data['city']
            self.tenantuser.country = self.cleaned_data['country']
            #self.tenantuser.postalcode = self.cleaned_data['postalcode']
            self.tenantuser.aboutme = self.cleaned_data['aboutme']
            self.tenantuser.save()
        return user