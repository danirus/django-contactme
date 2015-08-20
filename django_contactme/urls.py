from django import VERSION as DJANGO_VERSION

if DJANGO_VERSION[0:2] < (1, 4):
    from django.conf.urls.defaults import patterns, url
else:
    from django.conf.urls import patterns, url


urlpatterns = patterns(
    'django_contactme.views',
    url(r'^$', 'get_contact_form',
        name='contactme-get-contact-form'),
    url(r'^post/$', 'post_contact_form',
        name='contactme-post-contact-form'),
    url(r'^confirm/(?P<key>[^/]+)$', 'confirm_contact',
        name='contactme-confirm-contact'))
