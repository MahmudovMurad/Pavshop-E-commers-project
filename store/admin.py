from django.contrib.admin.options import ModelAdmin
from store.models import *
from django.contrib import admin
from django.utils.html import format_html

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 2

@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    model = ProductVersion
    extra = 2
    inlines = [ProductAttributeInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_cover_image')
    list_filter = ('price', 'brand')
    search_fields = ('name', 'price')
    fieldsets =(
        ("General informations", {
            'fields' : ('name', 'cover_image')
        }),

        ("About" , {
            'fields' : ('price', 'colors', 'brand', 'designer', 'quantity','category')
        }),

        ("Sale informations", {
            'fields' : ('sale_percant', 'discount_price', 'sale_time')
        }),
    )

    def get_cover_image(self, obj):
        str = "No Photo"
        if obj.cover_image:
            str = f'<img src="{obj.cover_image.url}" width="100" height ="100" />'
        return format_html(str)
    get_cover_image.short_description ='Cover_image'



admin.site.register(Review)
admin.site.register(Popular_Products)
admin.site.register(Color)
admin.site.register(Brand)

@admin.register(ProductAttribute)
class Attribute(admin.ModelAdmin):
    list_display = ('type', 'value' )


# admin.site.register(Basket)
admin.site.register(BasketItem)
class BasketItemInline(admin.ModelAdmin):
    list_display = ('user', 'product','quantity')

admin.site.register(Shopping_card)
admin.site.register(Category)