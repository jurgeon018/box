from import_export.resources import ModelResource
from box.core.utils import get_multilingual_fields

from .models import * 



class CurrencyResource(ModelResource):
    
    class Meta:
        model = Currency
        exclude = [
            'id',
            # 'code',
            'order',
            'is_active',
            'created',
            'updated',
        ]

    def get_export_order(self):
        multilingual_fields = get_multilingual_fields(self._meta.model)
        order = [
            "code",
            "sale_rate",
            "purchase_rate",
            "is_main",
            # *multilingual_fields['symbol'],
        ]
        return order 

    def get_import_id_fields(self):
        fields = [
            # 'id',
            'code',
        ]
        return fields 
    