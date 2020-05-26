from django.urls import path, include
from .views import GoogleMerchant
urlpatterns = [
  path('api/', include('box.apps.sw_shop.sw_catalog.api.urls')),
  path('google.xml/', GoogleMerchant()),
]
