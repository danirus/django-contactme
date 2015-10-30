import django
if django.VERSION[:2] < (1, 6):
    from django.conf.urls.defaults import patterns, include, url
else:
    from django.conf.urls import patterns, include, url

from django_contactme.tests import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^contact/', include('django_contactme.urls')),
    url(r'^qunit-tests$', views.qunit_tests, name="qunit-tests"),
)
urlpatterns += staticfiles_urlpatterns()
