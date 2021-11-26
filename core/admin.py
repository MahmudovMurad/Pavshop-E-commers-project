from django.contrib.admin.filters import ListFilter
from core.models import Subscriber, Tag,  Comment,Blog
from django.contrib import admin
from django.urls import resolvers

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'title', 'description')
    list_filter = ('name', 'title')


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('category',)
#     list_filter = ('category',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_filter = ('tag',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'active')
    list_filter = ('name', 'email')
