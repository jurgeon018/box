from django.core.management.base import BaseCommand
from box.apps.sw_shop.sw_catalog.models import (
  Item, ItemImage, ItemCategory, Attribute, AttributeValue, ItemAttribute, ItemAttributeValue
)
import random
import datetime 
import json 
import csv




class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    attributes = Attribute.objects.all().exclude(id__in=range(1,5))
    attribute_values = AttributeValue.objects.all().exclude(id__in=range(1,17))
    for i in range(1, 4):
      attribute, _ = Attribute.objects.get_or_create(name=f'атрибут {i}')

    for i in range(1, 10):
      value, _ = AttributeValue.objects.get_or_create(value=f'значення {i}')

    for i in range(1, 100):
      item, _  = Item.objects.get_or_create(title=f'товар {i}')
      item.category = random.choice(ItemCategory.objects.all()) 
      for j in range(1, 2):
        item_attribute, _ = ItemAttribute.objects.get_or_create(
          item=item,
          attribute=random.choice(attributes),
        )
        for k in range(1, 4):
          ItemAttributeValue.objects.get_or_create(
            item_attribute=item_attribute,
            value=random.choice(attribute_values), 
          )
      item.save()
      print(item)




