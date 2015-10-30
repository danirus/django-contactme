from django.shortcuts import render_to_response as render
from django.template import RequestContext


def homepage_v(request):
    return render("homepage.html", context_instance=RequestContext(request))


def qunit_test_v(request):
    return render("qunit_test.html", context_instance=RequestContext(request))

# --------------------------------------------------
from datetime import datetime, timedelta
from django_contactme import signals


def reject_email_with_xxx(sender, data, request, **kwargs):
    if 'xxx' in data['email']:
        return False

signals.confirmation_will_be_requested.connect(reject_email_with_xxx)


def check_submit_date_is_within_last_7days(sender, data, request, **kwargs):
    plus7days = timedelta(days=7)
    if data["submit_date"] + plus7days < datetime.now():
        return False

signals.confirmation_received.connect(check_submit_date_is_within_last_7days)
