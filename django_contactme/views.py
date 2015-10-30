from __future__ import unicode_literals

import json

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponseBadRequest, Http404)
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_GET, require_POST
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _

from django_contactme import get_form, signals, signed
from django_contactme.models import ContactMsg
from django_contactme.utils import send_mail


class ContactMsgPostBadRequest(HttpResponseBadRequest):
    """
    Response returned when a comment post is invalid. If ``DEBUG`` is on a
    nice-ish error message will be displayed (for debugging purposes), but in
    production mode a simple opaque 400 page will be displayed.
    """
    def __init__(self, why):
        super(ContactMsgPostBadRequest, self).__init__()
        if settings.DEBUG:
            self.content = render_to_string("django_contactme/400-debug.html",
                                            {"why": why})


def send_confirmation_email(data, key,
                            text_template=("django_contactme/"
                                           "confirmation_email.txt"),
                            html_template=("django_contactme/"
                                           "confirmation_email.html")):
    """
    Render message and send contact_msg confirmation email
    """
    site = Site.objects.get_current()
    subject = "[%s] %s" % (site.name, _("contact message confirmation request"))
    confirmation_url = reverse("contactme-confirm-contact", args=[key])
    message_context = Context({'data': data,
                               'confirmation_url': confirmation_url,
                               'support_email': settings.DEFAULT_FROM_EMAIL,
                               'site': site})
    text_message_template = loader.get_template(text_template)
    text_message = text_message_template.render(message_context)
    html_message_template = loader.get_template(html_template)
    html_message = html_message_template.render(message_context)
    send_mail(subject, text_message, settings.DEFAULT_FROM_EMAIL,
              [data['email']], html=html_message)


def send_contact_received_email(contact_msg,
                                template=("django_contactme/"
                                          "contact_received_email.txt")):
    site = Site.objects.get_current()
    subject = "[%s] %s" % (site.name, _("new contact request"))
    message_template = loader.get_template(template)
    message_context = Context({'contact_msg': contact_msg, 'site': site})
    message = message_template.render(message_context)
    if getattr(settings, "CONTACTME_NOTIFY_TO", False):
        if len(settings.CONTACTME_NOTIFY_TO.split(",")) > 0:
            notify_to = settings.CONTACTME_NOTIFY_TO.split(",")
        else:
            notify_to = [settings.CONTACTME_NOTIFY_TO]
    else:
        notify_to = ["%s <%s>" % (name, email)
                     for name, email in settings.ADMINS]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, notify_to)


@require_GET
def get_contact_form(request, next=None,
                     template="django_contactme/contactme.html"):
    return render_to_response(template, {"next": next}, RequestContext(request))


@csrf_protect
@require_POST
def post_contact_form(request, next=None,
                      template_preview="django_contactme/preview.html",
                      template_discarded="django_contactme/discarded.html",
                      template_post="django_contactme/confirmation_sent.html"):
    """
    Post a contact message.

    HTTP POST is required. If ``POST['submit'] == "preview"`` or if there are
    errors a preview template, ``comments/preview.html``, will be rendered.
    """
    data = request.POST.copy()

    # Check to see if the POST data overrides the view's next argument.
    next = data.get("next", next)

    # Do we want to preview the message?
    preview = "preview" in data

    # Construct the form
    form = get_form()(data=data)

    # Check security information
    if form.security_errors():
        return ContactMsgPostBadRequest(
            "The contact message form failed security verification: %s" %
            escape(str(form.security_errors())))

    # If there are errors or if we requested a preview show the comment
    if form.errors or preview:
        return render_to_response(template_preview,
                                  {"form": form, "next": next},
                                  RequestContext(request, {}))

    contact_msg_data = form.get_instance_data()

    # Signal that a confirmation is about to be requested
    responses = signals.confirmation_will_be_requested.send(
        sender=form.__class__, data=contact_msg_data, request=request)

    # Check whether a signal receiver decides to kill the process
    for (receiver, response) in responses:
        if response is False:
            return render_to_response(template_discarded,
                                      {'data': contact_msg_data},
                                      context_instance=RequestContext(request))

    # Create key and send confirmation URL by email
    key = signed.dumps(contact_msg_data, compress=True,
                       extra_key=settings.CONTACTME_SALT)
    send_confirmation_email(contact_msg_data, key)

    # Signal that a confirmation has been requested
    signals.confirmation_requested.send(sender=form.__class__,
                                        data=contact_msg_data,
                                        request=request)

    if next is not None:
        return HttpResponseRedirect(next)

    return render_to_response(template_post,
                              context_instance=RequestContext(request))


@csrf_protect
@require_POST
def post_ajax_contact_form(
        request,
        template_preview="django_contactme/preview_ajax.html",
        template_discarded="django_contactme/discarded_ajax.html",
        template_post="django_contactme/confirmation_sent_ajax.html",
        template_field_errors="django_contactme/field_errors.html"):
    """
    Post a contact message via AJAX.

    HTTP POST is required. If ``POST['submit'] == "preview"`` or if there are
    errors a preview template, ``django_contactme/ajax_preview.html``, will
    be rendered.
    """
    if not request.is_ajax():
        return HttpResponseBadRequest("Bad request, AJAX call expected.")

    post_data = request.POST.copy()
    preview = "preview" in post_data  # want to preview the message?
    form = get_form()(data=post_data)  # Construct the form

    # Check security information
    if form.security_errors():
        return ContactMsgPostBadRequest(
            "The contact message form failed security verification: %s" %
            escape(str(form.security_errors())))

    json_data = {}
    if form.errors:
        json_data.update({'status': 'errors', 'errors': {}})
        for field_name in form.errors:
            json_data['errors'][field_name] = render_to_string(
                template_field_errors,
                {'field': form[field_name]},
                RequestContext(request, {}))

    if preview or form.errors:
        json_data['html'] = render_to_string(template_preview, {'form': form})
        if not form.errors:
            json_data['status'] = 'preview'
        return HttpResponse(json.dumps(json_data),
                            content_type='application/json')

    contact_msg_data = form.get_instance_data()

    # Signal that a confirmation is about to be requested
    responses = signals.confirmation_will_be_requested.send(
        sender=form.__class__, data=contact_msg_data, request=request)

    # Check whether a signal receiver decides to kill the process
    for (receiver, response) in responses:
        if response is False:
            html = render_to_string(template_discarded,
                                    {'data': contact_msg_data},
                                    context_instance=RequestContext(request))
            payload = json.dumps({'status': 'discarded', 'html': html})
            return HttpResponse(payload, content_type='application/json')

    # Create key and send confirmation URL by email
    key = signed.dumps(contact_msg_data, compress=True,
                       extra_key=settings.CONTACTME_SALT)
    send_confirmation_email(contact_msg_data, key)

    # Signal that a confirmation has been requested
    signals.confirmation_requested.send(sender=form.__class__,
                                        data=contact_msg_data,
                                        request=request)

    html = render_to_string(template_post,
                            context_instance=RequestContext(request))
    payload = json.dumps({'status': 'success', 'html': html})
    return HttpResponse(payload, content_type='application/json')


def confirm_contact(request, key,
                    template_accepted="django_contactme/accepted.html",
                    template_discarded="django_contactme/discarded.html"):
    try:
        data = signed.loads(key, extra_key=settings.CONTACTME_SALT)
    except (ValueError, signed.BadSignature):
        raise Http404

    # Check that the URL is not confirmed yet otherwise return a Http404
    exists = (ContactMsg.objects.filter(
        name=data['name'], email=data['email'],
        submit_date=data['submit_date']).count() > 0)
    if exists:
        raise Http404

    # Signal that the contact_message is about to be saved
    responses = signals.confirmation_received.send(
        sender=ContactMsg, data=data, request=request)

    # Check whether a signal receiver decides to discard the contact_msg
    for (receiver, response) in responses:
        if response is False:
            return render_to_response(template_discarded, {'data': data},
                                      context_instance=RequestContext(request))

    # Create ContactMsg object
    # - note: The submit_date read in the key may be used as well to discard
    #         messages older than a certain date. Read the docs for an example.
    #         http://readthedocs.org/projects/django-contactme
    contact_msg = ContactMsg.objects.create(site_id=settings.SITE_ID,
                                            name=data['name'],
                                            email=data['email'],
                                            message=data['message'],
                                            submit_date=data['submit_date'])
    contact_msg.ip_address = request.META.get("REMOTE_ADDR", None)
    contact_msg.save()

    # Notify Admins about the new ContactMsg
    send_contact_received_email(contact_msg)

    return render_to_response(template_accepted, {'data': data},
                              context_instance=RequestContext(request))
