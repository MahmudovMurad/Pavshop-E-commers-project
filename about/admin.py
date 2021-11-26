from django.contrib import admin
from django.db import models
from about.models import  Shipping_info,Billing_data, ZipCode, Order,Wishlist
from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
@admin.register(Shipping_info)
class Shipping_infoAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'address', 'country',)
    list_filter = ('name', 'phone', 'address',)
    search_fields = ('name',)
    fieldsets =(
        ("General informations", {
            'fields' : ('name', 'surname', 'email', 'phone')
        }),
    )

@admin.register(Billing_data)
class Billing_dataAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'address', 'country',)
    list_filter = ('name', 'phone', 'address',)
    search_fields = ('name',)
    fieldsets =(
        ("General informations", {
            'fields' : ('name', 'surname', 'email', 'phone')
        }),
    )
admin.site.register(Wishlist)
admin.site.register(ZipCode)
admin.site.register(Order)