from django import forms
from about.models import *
from django.contrib.auth import get_user_model, password_validation
from django.db.models.fields.related import OneToOneField
from django.forms.fields import CharField
from django.shortcuts import render
from contact.models import *
from about.models import Billing_data
from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth.forms import (
    PasswordChangeForm, UserCreationForm, UsernameField, AuthenticationForm,PasswordResetForm,SetPasswordForm
)

User = get_user_model()


class BillingData(forms.ModelForm):
    class Meta:
        model = Billing_data
        fields = ['name', 'surname', 'email', 'phone', 'company_name', 'address', 'city_town', 'country', 'email', 'phone']

    def save(self, commit=True):
      return super().save(commit=commit)

# class ShippingInfo(forms.ModelForm):
#     class Meta:
#         model = Shipping_info
#         fields = '__all__'

#     def save(self, commit=True):
#       return super().save(commit=commit)