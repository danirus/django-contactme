from django.conf.urls import include, url
from django.contrib import admin

from views import homepage_v


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('django_contactme.urls')),
    url(r'^$', homepage_v, name='homepage'),    
]
