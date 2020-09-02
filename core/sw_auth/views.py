from django.shortcuts import redirect, reverse 
from django.contrib.auth import logout

from . import settings as auth_settings 

def sw_logout(request):
    logout(request)
    x = auth_settings.LOGOUT_REDIRECT_URL
    return redirect(reverse(x))





