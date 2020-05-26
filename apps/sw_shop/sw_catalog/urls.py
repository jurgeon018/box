from django.urls import path, include, reverse
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


class CustomSyndicationFeed(SyndicationFeed):
    mime_type = 'application/xml'
    content_type = 'application/xml'

    def write(self, outfile, encoding):
        handler = SimplerXMLGenerator(outfile, encoding)
        handler.startDocument()
        handler.startElement("root", self.root_attributes())
        # self.add_root_elements(handler)
        # self.write_items(handler)
        # handler.endElement("root")

    # def add_root_elements(self, handler):
    #     # Add root elements here
    #     handler.addQuickElement("my_feed_title", self.feed['title'])
    #     handler.addQuickElement("my_feed_url", self.feed['link'])

    # def write_items(self, handler):
    #     for item in self.items:
    #         handler.startElement('my_item', self.item_attributes(item))
    #         self.add_item_elements(handler, item)
    #         handler.endElement("my_item")

    # @staticmethod
    # def _safe_add_element(handler, item, attr):
    #     # Add attribute to xml only if it is present, no empty tags
    #     if item.get(attr):
    #         handler.addQuickElement(attr, item[attr])

    # def add_item_elements(self, handler, item):
    #     # Handle each element that needs to be added to an xml item
    #     # 'item' is a dict of attributes
    #     handler.addQuickElement('title', item['title'])
    #     # handler.addQuickElement('date', item['date'])
    #     # handler.addQuickElement('link', item['link'])
    #     handler.addQuickElement('description', item['description'])

    #     self._safe_add_element(handler, item, 'city')
    #     self._safe_add_element(handler, item, 'postalcode')


class CorrectMimeTypeFeed(Rss201rev2Feed):
  content_type = 'application/xml; charset=utf-8'

class LatestEntriesFeed(Feed):
  title = "Faina Vishivanka"
  link = "/"
  description = "Items from shop"
  feed_type = CorrectMimeTypeFeed
  
  def items(self):
      return Item.objects.all()[:10]

  def item_title(self, item):
      return item.title

  def item_description(self, item):
      return item.description

  # item_link is only needed if NewsItem has no get_absolute_url method.
  def item_link(self, item):
      return reverse('item', args=[item.slug])

  # def get_context_data(self, **kwargs):
  #     context = super().get_context_data(**kwargs)
  #     context['foo'] = 'bar'
  #     return context





urlpatterns = [
  path('api/', include('box.apps.sw_shop.sw_catalog.api.urls')),
  path('google.xml/', LatestEntriesFeed()),
]
