from django.shortcuts import redirect 
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from ..models import *
from box.core.mail import box_send_mail 

from django.utils.translation import ugettext_lazy as _
 

import json 
from rest_framework.decorators import api_view

# @csrf_exempt
@api_view(['GET', 'POST'])
def sw_contact(request):
    # query = request.body.decode('utf-8')
    # query = json.loads(query)
    query    = request.POST or request.GET
    if not query:
        query = request.data 
    name     = query.get('name',    '---')
    email    = query.get('email',   '---')
    phone    = query.get('phone',   '---')
    message  = query.get('message', '---')
    url      = request.META.get('HTTP_REFERER')
    model    = Contact.objects.create(
        name=name,
        email=email,
        phone=phone,
        message=message,
        url=url
    )
    box_send_mail(
      subject      = _('Отримано контактну форму'),
      template     = 'sw_contact_form/mail.html', 
      email_config = ContactRecipientEmail, 
      model        = model, 
      fail_silently= False,
    )
    return JsonResponse({
        'status':'OK',
    })






