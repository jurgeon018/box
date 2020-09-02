from django.conf import settings 

def get(x, y):
    return getattr(settings, x, y)

LOGIN_REDIRECT_URL    = get('LOGIN_REDIRECT_URL', 'profile')
LOGOUT_REDIRECT_URL   = get('LOGOUT_REDIRECT_URL', 'index')
REGISTER_REDIRECT_URL = get('REGISTER_REDIRECT_URL', 'profile')
