from django.conf import settings 


DEFAULT_DELIVERY_AUTO_PUBLIC_API_KEY = 'DE071A11-7F7A-EA11-81BF-000D3A20E396'
DELIVERY_AUTO_PUBLIC_API_KEY = getattr(
    settings, 'DELIVERY_AUTO_PUBLIC_API_KEY', DEFAULT_DELIVERY_AUTO_PUBLIC_API_KEY)

DEFAULT_DELIVERY_AUTO_SECRET_API_KEY = 'fb74c74d7b110e67e690bf3dbf897a3c'
DELIVERY_AUTO_SECRET_API_KEY = getattr(
    settings, 'DELIVERY_AUTO_SECRET_API_KEY', DEFAULT_DELIVERY_AUTO_SECRET_API_KEY)




