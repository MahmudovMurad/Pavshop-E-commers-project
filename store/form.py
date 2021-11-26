from django import forms
from django.contrib.auth import get_user_model 
from django.shortcuts import render
from store.models import *
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    PasswordChangeForm, UserCreationForm, UsernameField, AuthenticationForm,PasswordResetForm,SetPasswordForm
)
User = get_user_model()


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email', 'message','profile_img')

        def save(self, commit=True):
            return super().save(commit=commit)




# class ShippinginfoForm(forms.ModelForm):
#     name = forms.CharField(max_length=30)
#     surname = forms.CharField(max_length=40)
#     email = forms.EmailField(max_length=100)
#     phone = forms.IntegerField()
#     company = forms.CharField(max_length=50)
#     address = forms.CharField(max_length=255)
#     country = forms.CharField(max_length=255)
#     town = forms.CharField(max_length=255)

#     class Meta:
#         model = User
        

# class BillingdataForm(forms.ModelForm):
#     name = forms.CharField(max_length=30)
#     surname = forms.CharField(max_length=40)
#     email = forms.EmailField(max_length=100)
#     phone = forms.IntegerField()
#     company = forms.CharField(max_length=50)
#     address = forms.CharField(max_length=255)
#     country = forms.CharField(max_length=255)
#     town = forms.CharField(max_length=255)

#     class Meta:
#         model = User
           

