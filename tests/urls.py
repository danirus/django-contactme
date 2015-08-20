from django.conf.urls import patterns, include

urlpatterns = patterns('',
    (r'^contact/', include('django_contactme.urls')),
)
