from django.contrib import admin 
from django.utils.html import mark_safe 
from django.utils.translation import gettext_lazy as _
from .models import *

from box.custom_auth.admin import CustomUserAdmin



class CustomerAdmin(CustomUserAdmin):
    pass


class CustomerGroupAdmin(admin.ModelAdmin):
    def coupon(self, obj):
        if obj.coupon:
            return mark_safe(f'<a href="/admin/customer/coupon/{obj.coupon.id}/change">{obj.coupon.name}</a>')
        return '---'
    list_display = [
        'name',
        'coupon',
    ]
    list_display_links = list_display
    autocomplete_fields = [
        'coupon',
    ]
    search_fields = [
        'name',
    ]


class CouponAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]
    list_display = [
        "name",
        "discount_amount",
        "discount_type",
        "requisition",
        "period",
        "one_time",
        "uses_amount",
    ]
    list_display_links = [
        'name',
        # ''
    ]
    list_editable = [
        "discount_amount",
        "discount_type",
        "requisition",
        "period",
        "one_time",
    ]
    fields = [
        "name",
        (
        "discount_amount",
        "discount_type",
        "requisition",
        ),
        "period",
        "one_time",
        "uses_amount",
    ]
    readonly_fields = [
        'uses_amount',
    ]


class SubscriberAdmin(admin.ModelAdmin):
    list_display = [
        'email'
    ]
    list_display_links = list_display




# from box.shop.customer.admin import (
#     CustomerGroup, CustomerGroupADmin
#     Coupon, CouponADmin
#     Subscriber, SubscriberADmin
# )
admin.site.register(CustomerGroup, CustomerGroupAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Subscriber, SubscriberAdmin)

