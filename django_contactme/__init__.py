"""
django_contactme - Contact form pluggable django app with email verification
"""
from django_contactme.conf import settings
from django.utils.module_loading import import_string


default_app_config = 'django_contactme.apps.ContactMeConfig'
    
def get_form():
    return import_string(settings.CONTACTME_FORM_CLASS)
    

VERSION = (1, 3, 0, 'f', None) # following PEP 386

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3] != 'f':
        version = '%s%s%s' % (version, VERSION[3], VERSION[4])
    return version
