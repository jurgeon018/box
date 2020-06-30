from django.contrib import admin 
from ..models.features import * 

import nested_admin 


class ItemFeatureInline(nested_admin.NestedTabularInline):
    model = ItemFeature
    # model = ItemFeature.items.through
    extra = 0
    autocomplete_fields = [
        'name',
        'value',
    ]
    # classes 




@admin.register(ItemFeature)
class ItemFeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(FeatureValue)
class FeatureValueAdmin(admin.ModelAdmin):
    search_fields = ['value']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    search_fields = ['name']


    


































