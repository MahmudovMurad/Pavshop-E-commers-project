from django import forms
from django.forms.forms import Form
from django.views.generic.edit import FormView
from core.models import *
from django.contrib.auth import get_user_model, password_validation
from django.forms import fields
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import get_user_model

from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
     UserCreationForm, UsernameField, AuthenticationForm,SetPasswordForm
)
User = get_user_model()


class SubscribeForm(forms.ModelForm):
  class Meta:
    model = Subscriber
    fields = ['email']

    def save(self, commit=True):
      return super().save(commit=commit)


# class CommentForm(AuthenticationForm):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100)
#     subject = forms.CharField(max_length=255)
#     comment = forms.CharField(max_length=255)

  
class BlogListForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = ['title', 'description', 'img', 'name', 'tags']

    def save(self, commit=True):
      return super().save(commit=commit)