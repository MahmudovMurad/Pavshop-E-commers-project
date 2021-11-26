from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField, BooleanField, DateTimeField
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from .models import*


class CustomUserManager(BaseUserManager):

    def create_user(self, name, email, password, surname):
        user = self.model(name=name, email=email, surname=surname)
        user.set_password(password)
        user.save()

        return user
    

    def create_superuser(self, name, email, password, surname):

        user = self.create_user(name, email, password, surname)
        user.is_staff = True
        user.is_superuser =True
        user.is_active = True
        user.save()

        return user
    


class User(AbstractBaseUser, PermissionsMixin):
    """
    user login details
    """
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=100, null=True ,blank= True)
    image = models.ImageField(upload_to = 'profile_pictures', blank=True, null = True)
    address1 = models.CharField(max_length=100, blank=True, null = True)
    address2 = models.CharField(max_length=100,blank=True, null = True)
    country_state = models.CharField(max_length=100, blank=True,null=True)
    town = models.CharField(max_length=100, blank=True, null = True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']
    objects = CustomUserManager()

    def get_username(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def __str__(self) -> str:
        return self.email

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=200)