priority_third_party = [
    'corsheaders',
    'box.sw_admin',  
    # 'admin_tools', 'admin_tools.theming', 'admin_tools.menu', 'admin_tools.dashboard',
    'dal',
    'dal_select2',
    'admin_auto_filters',
    'modeltranslation',
]
django_contrib = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
]
third_party = [
    "mptt",
    "crispy_forms",
    "tinymce",
    'ckeditor',
    'ckeditor_uploader',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'import_export',
    'rosetta',
    'colorfield',
    'adminsortable2',
    "rest_framework",
    'rest_framework.authtoken',
    "djoser",
    "rangefilter",
]
box_core = [
    'box.core',
    'box.core.sw_novaposhta',
    'box.core.sw_global_config',
    'box.core.sw_solo',
    'box.core.sw_model_search',
    'box.core.sw_content',
    'box.core.sw_contact_form',
    'box.core.sw_auth',
]
box_shop = [
    'box.shop',
    'box.sw_shop.item',
    'box.sw_shop.order',
    'box.sw_shop.cart',
    'box.sw_shop.customer',
]
box_payment = [
    'box.sw_payment.liqpay',
    'box.sw_payment.wayforpay',
    'box.sw_payment.interkassa',
]
box_blog = [
    'box.sw_blog',
]
INSTALLED_APPS  = [
    *priority_third_party,
    *django_contrib,
    *third_party,
    *box_core,
    *box_shop,
    *box_payment,
    *box_blog,
]


