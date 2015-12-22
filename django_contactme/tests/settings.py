from __future__ import unicode_literals

import os

PRJ_PATH = os.path.abspath(os.path.curdir)

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.sqlite3',
        'NAME':     'django_contactme_test',
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
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

STATIC_URL = "/static/"

SECRET_KEY = 'v2824l&2-n+4zznbsk9c-ap5i)b3e8b+%*a=dxqlahm^%)68jn'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_contactme.tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'DIRS': [
	    os.path.join(os.path.dirname(__file__), "templates"),
	    os.path.join(os.path.dirname(__file__), "..", "templates"),
	],
        'APP_DIRS': True,
	'OPTIONS': {
	    'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
	    ],
	},
    },
]

INSTALLED_APPS = [
    'django_contactme.apps.ContactMeConfig',
    'django_contactme.tests.apps.ContactMeTestsConfig',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

DEFAULT_FROM_EMAIL = "Alice Bloggs <alice@example.com>"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CONTACTME_SALT = b"es-war-einmal-una-bella-princesa-in-a-beautiful-castle"
CONTACTME_NOTIFY_TO = "Joe Bloggs <joe.bloggs@example.com>"
