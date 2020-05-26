from django.utils.feedgenerator import (
  Atom1Feed,
  Rss201rev2Feed ,
  RssUserland091Feed ,
  Atom1Feed,
  SyndicationFeed,
)

from django.contrib.syndication.views import Feed
from django.utils.xmlutils import SimplerXMLGenerator
from .models import Item


class GoogleProductsFeed(Rss201rev2Feed):
  content_type = 'application/xml; charset=utf-8'

  def rss_attributes(self):
      attrs = super().rss_attributes()
      attrs['xmlns:g'] = 'http://base.google.com/ns/1.0'
      attrs['xmlns:c'] = 'http://base.google.com/cns/1.0'
      return attrs

  def add_item_elements(self, handler, item):
    super().add_item_elements(handler, item)
    if item.get('id') is not None:
      handler.addQuickElement(u"g:id", item['id'])
    if item.get('mpn') is not None:
      handler.addQuickElement(u"g:mpn", item['mpn'])
    if item.get('condition') is not None:
      handler.addQuickElement(u"g:condition", item['condition'])
    if item.get('price') is not None:
      handler.addQuickElement(u"g:price", item['price'])
    if item.get('availability') is not None:
      handler.addQuickElement(u"g:availability", item['availability'])
    if item.get('brand') is not None:
      handler.addQuickElement(u"g:brand", item['brand'])
    if item.get('adult') is not None:
      handler.addQuickElement(u"g:adult", item['adult'])
    if item.get('product_type') is not None:
      handler.addQuickElement(u"g:product_type", item['product_type'])
    if item.get('image_links') is not None:
      key = u"g:image_link"
      for img in item['image_links']:
          handler.addQuickElement(key, img)
          key = u"g:additional_image_link"

from django.contrib.sites.models import Site 
from .models import ItemImage 

class GoogleMerchant(Feed):
  title = "Faina Vishivanka"
  link = "/"
  description = "Items from shop"
  feed_type = GoogleProductsFeed

  def items(self):
    # items = Item.objects.all() \
            # .filter(in_stock__availability=True) \ 
            # .filter(currency__isnull=False)
    # return items
    return Item.objects.all().filter(
      currency__isnull=False,
      in_stock__availability=True,
    )

  def item_title(self, item):
      return item.title

  def item_description(self, item):
      return item.description

  def item_extra_kwargs(self, item):
    image_links = []
    current_site = Site.objects.get_current().domain
    for image in ItemImage.objects.filter(item=item):
      image_links.append(f'https://{current_site}{image.image.url}')
    product_type = item.category.tree_title.replace('->','>') 
    item_data = {
        "id":str(item.id),
        "mpn":str(item.id),
        "condition":"new",
        "price":f'{item.price} {item.currency.code.upper()}',
        "availability":"in_stock",
        "brand":getattr(item.brand, "title", None),
        "adult":"false",
        "product_type":product_type,
        "image_links":image_links,
    }
    return item_data




