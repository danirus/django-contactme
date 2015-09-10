import django
if django.VERSION[:2] < (1, 6):
    from django.conf.urls.defaults import patterns, include, url
else:
    from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('django_contactme.urls')),
    url(r'^$',        'homepage_v', name='homepage'),
)
