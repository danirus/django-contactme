from django.shortcuts import render_to_response as render
from django.template import RequestContext


def qunit_tests(request):
    return render("django_contactme/jquery_plugin_tests.html",
                  context_instance=RequestContext(request))
