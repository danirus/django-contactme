import django

if django.VERSION[:2] < (1, 6):
    from django.conf.urls.defaults import patterns, url
elif django.VERSION[:2] < (1, 9):
    from django.conf.urls import patterns, url
else:
    from django.conf.urls import url
    
from django_contactme.views import (get_contact_form, post_contact_form,
				    post_ajax_contact_form, confirm_contact)


url_list = [
    url(r'^$', get_contact_form,
        name='contactme-get-contact-form'),
    url(r'^post/$', post_contact_form,
        name='contactme-post-contact-form'),
    url(r'^post/ajax$', post_ajax_contact_form,
	name='contactme-post-ajax-contact-form'),
    url(r'^confirm/(?P<key>[^/]+)$', confirm_contact,
        name='contactme-confirm-contact')
]

if django.VERSION[:2] < (1, 9):
    urlpatterns = patterns('django_contactme.views', url_list)
else:
    urlpatterns = url_list
