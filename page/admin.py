from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import *


class PageFeatureInline(admin.TabularInline):
    model = PageFeature
    extra = 0
    classes = ['collapse']
    exclude = [
        'code',
    ]


class PageAdmin(TabbedTranslationAdmin):
    inlines = [
        PageFeatureInline, 

    ]
    list_display_links = [
        "id",
        'meta_title',
        'code',
    ]
    list_display = [
        "id",
        'meta_title',
        'code',
    ]
    fieldsets = [
        [('SEO'), {
            'fields':(
                'meta_title',
                'meta_descr',
                'meta_key',
            ),
            'classes':(
                'wide', 
                'extrapretty',
            ),
        }],
    ]
    search_fields = [
        'meta_title',
    ]

class PageFeatureAdmin(TabbedTranslationAdmin):
    list_display_links = [
        "id",
        'code',
        # 'name',
        'page',
    ]
    list_display = [
        "id",
        'code',
        # 'name',
        'page',
        # 'value',
    ]
    list_editable = [
        # 'value'
    ]
    exclude  = [
    ]


class PageImageAdmin(TabbedTranslationAdmin):
    list_display_links = [
        "id",
        'code',
        # 'name',
        'value',
    ]
    list_display = [
        "id",
        'code',
        # 'name',
        'value',
    ]
    exclude  = [
        'page',
    ]

