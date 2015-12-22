from __future__ import unicode_literals

import imp
import os

PRJ_PATH = os.path.abspath(os.path.curdir)

DEBUG = True

ADMINS = (
    ('Alice Bloggs', 'alice@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.sqlite3',
        'NAME':     'django_contactme_demo.db',
        'USER':     '',
        'PASSWORD': '',
        'HOST':     '',
        'PORT':     '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Brussels'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PRJ_PATH, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# STATIC_ROOT = os.path.join(PRJ_PATH, 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PRJ_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'v2824l&2-n+4zznbsk9c-ap5i)b3e8b+%*a=dxqlahm^%)68jn'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'DIRS': [
	    os.path.join(os.path.dirname(__file__), "templates"),
	],
        'APP_DIRS': True,
	'OPTIONS': {
	    'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
		'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
	    ],
	},
    },
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    "django.contrib.staticfiles",

    'crispy_forms',
    'django_contactme',
)

# EMAIL_HOST          = "smtp.gmail.com"
# EMAIL_PORT          = "587"
# EMAIL_HOST_USER     = ""
# EMAIL_HOST_PASSWORD = ""
# EMAIL_USE_TLS       = True # Yes for Gmail
DEFAULT_FROM_EMAIL = "Alice Bloggs <alice@example.com>"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Fill in actual EMAIL settings above, and comment out the
# following line to let this django demo sending emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CONTACTME_SALT = b"es-war-einmal-una-bella-princesa-in-a-beautiful-castle"
CONTACTME_NOTIFY_TO = "Your Name <youruser@yourdomain>"
# CONTACTME_FORM_CLASS = "crispy_forms_demo.forms.CrispyContactMsgForm"
CONTACTME_FORM_CLASS = "crispy_forms_demo.forms.CrispyContactMsgForm"

CRISPY_TEMPLATE_PACK = 'bootstrap3'
