import django

if django.VERSION[:2] < (1, 6):
    from django.conf.urls.defaults import include, patterns, url
elif django.VERSION[:2] < (1, 9):
    from django.conf.urls import include, patterns, url
else:
    from django.conf.urls import include, url

from django.contrib import admin
from views import homepage_v

admin.autodiscover()


url_list = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('django_contactme.urls')),
    url(r'^$', homepage_v, name='homepage'),    
]

if django.VERSION[:2] < (1, 9):
    urlpatterns = patterns('', url_list)
else:
    urlpatterns = url_list
