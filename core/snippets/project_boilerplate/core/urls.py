from box.urls import * 

from django.urls import path, include

urlpatterns = [
  path('', include('box.urls')),
  path('', include('project.api.urls')),
]

multilingual_urls = [
  path('', include('box.multilingual_urls')),
  path('', include('project.urls')),
]

from django.conf import settings 
from django.conf.urls.i18n import i18n_patterns


urlpatterns += i18n_patterns(
  path('', include(multilingual_urls)),
  prefix_default_language=settings.USE_I18N,
)



