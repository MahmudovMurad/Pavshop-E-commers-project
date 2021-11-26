from django.db import models
from contact.models import  User, ContactModel
from django.contrib import admin
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'phone',)
    search_fields = ('email',)
    
admin.site.register(ContactModel)
