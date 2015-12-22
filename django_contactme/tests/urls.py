from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django_contactme.tests import views


urlpatterns = [
    url(r'^contact/', include('django_contactme.urls')),
    url(r'^qunit-tests$', views.qunit_tests, name="qunit-tests"),    
]
urlpatterns += staticfiles_urlpatterns()
