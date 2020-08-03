from django.core.management.base import BaseCommand
# import csv
# from datetime import datetime 
# from pathlib import Path
# from datetime import datetime 
# from io import StringIO, BytesIO
# from tablib import Dataset
# from box.core.utils import get_resource, get_resources

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site 

class Command(BaseCommand):

  def add_arguments(self, parser):
    # parser.add_argument(
    #     '-e',
    #     '--extention',
    # )
    parser.add_argument(
        '-p',
        '--provider',
    )
    parser.add_argument(
        '-n',
        '--name',
    )
    parser.add_argument(
        '-c',
        '--client_id',
    )
    parser.add_argument(
        '-s',
        '--secret',
    )
    parser.add_argument(
        '-k',
        '--key',
    )

  def handle(self, *args, **kwargs):
    '''
    https://console.developers.google.com/apis/credentials?project=mynewagent-65760&authuser=4

    python3 manage.py gen_social_app -p google -n google -c 697687398766-c0bp6htapgjknp375e62arb8njtutt2i.apps.googleusercontent.com 
    '''
    provider  = kwargs.get('provider',)
    name      = kwargs.get('name',)
    client_id = kwargs.get('client_id',)
    secret    = kwargs.get('secret',)
    if not provider:
        provider = 'google'
    if not name:
        name = 'google'
    if not client_id:
        client_id = '697687398766-c0bp6htapgjknp375e62arb8njtutt2i.apps.googleusercontent.com'
    if not secret:
        secret = 'qG1YSFzKX40VlMdBgxLTRBpI'
    # key       = kwargs.get('key', '')
    # sites     = kwargs.get('sites')
    social_app, _ = SocialApp.objects.get_or_create(
        provider=provider,
        name=name,
        client_id=client_id,
        secret=secret,
        # key=key,
        # sites=sites,
    )
    site = Site.objects.get_current()
    social_app.sites.add(site)
    social_app.save()
    print('ok')



