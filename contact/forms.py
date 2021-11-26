from django import forms

from django.contrib.auth import get_user_model, password_validation
from django.db.models.fields.related import OneToOneField
from django.forms.fields import CharField
from django.shortcuts import render
from contact.models import *
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    PasswordChangeForm, UserCreationForm, UsernameField, AuthenticationForm,PasswordResetForm,SetPasswordForm
)

User = get_user_model()

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'phone', 'subject', 'message']

    def save(self, commit=True):
      return super().save(commit=commit)


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        help_text=password_validation.password_validators_help_text_html(),
        
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
   
    class Meta:
        model = User
        fields = (
            'name',
            'surname',
            'email',
            'phone',
            'password1',
            'password2',
            'address1',
            'address2',
            'country_state',
            'town'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'address1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
            'address2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            'town': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Town'
            }),
        }



class LoginForm(AuthenticationForm):
    
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }), max_length=254)
    
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        }),
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }), max_length=254)



class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password'
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),

    )

    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        }),
    )

class CustomChangePasswordForm(PasswordChangeForm):
    old_password1 = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Change Password'
            }),
    )   
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password1'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password1'}),
    )
    
 
 
def password_success(request):
    return render(request, 'password-success.html', {})



    