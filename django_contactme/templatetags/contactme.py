from django import template
from django.template.loader import render_to_string

from django_contactme import get_form
# from django_contactme.forms import ContactMsgForm


register = template.Library()


class ContactFormNode(template.Node):
    def render(self, context):
        context.push()
        form_str = render_to_string("django_contactme/form.html",
                                    {"form": get_form()()},
                                    context)
        context.pop()
        return form_str


def render_contact_form(parser, token):
    """
    Render the contact form (as returned by ``{% render_contact_form %}``)
    through the ``django_contactme/form.html`` template.

    Syntax::

        {% render_contact_form %}
    """
    return ContactFormNode()

register.tag(render_contact_form)
