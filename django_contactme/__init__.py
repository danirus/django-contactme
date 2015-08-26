"""
django_contactme - Contact form pluggable django app with email verification
"""
import django
from django_contactme.conf import settings

if django.VERSION[:2] <= (1, 5): # Django <= 1.5
    from django_contactme.compat import import_by_path as import_string
elif (1, 6) <= django.VERSION[:2] < (1, 8): # Django v1.6.x and 1.7.x
    from django.utils.module_loading import import_by_path as import_string
else: # Django >= 1.8
    from django.utils.module_loading import import_string

    
def get_form():
    return import_string(settings.CONTACTME_FORM_CLASS)
    

VERSION = (1, 2, 1, 'f', None) # following PEP 386

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3] != 'f':
        version = '%s%s%s' % (version, VERSION[3], VERSION[4])
    return version
