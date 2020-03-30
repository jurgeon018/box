from django.contrib.sitemaps import Sitemap 
from django.urls import reverse 
from django.conf import settings 


class StaticSitemap(Sitemap):

    changefreq = 'weekly' # | 'never'
    priority = 1
    protocol = 'https'
    i18n = True 

    def items(self):
        return settings.STATIC_SITEMAP_PAGES 
        
    def location(self, item):
        return reverse(item)

