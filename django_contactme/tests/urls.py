from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('',
    (r'^contact/', include('django_contactme.urls')),
)
