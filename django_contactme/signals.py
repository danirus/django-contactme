"""
Signals relating to django-contactme.
"""
from django.dispatch import Signal


confirmation_will_be_requested = Signal(providing_args=["data", "request"])
confirmation_will_be_requested.__doc__ = """
Sent just before a confirmation message is requested.

A message is sent to the user right after the contact form is been posted and
validated to verify the user's email address. This signal may be used to ban
email addresses or check message content. If any receiver returns False the
process is discarded and the user receives a discarded message.
"""


confirmation_requested = Signal(providing_args=["data", "request"])
confirmation_requested.__doc__ = """
Sent just after a confirmation message is requested.

A message is sent to the user right after the contact form is been posted
and validated to verify the user's email address. This signal may be uses to
trace contact messages posted but never confirmed.
"""


# Sent just after a contact_msg has been verified.
confirmation_received = Signal(providing_args=["data", "request"])
confirmation_received.__doc__ = """
Sent just after a confirmation has been received.

A confirmation is received when the user clicks on the link provided in the
confirmation message sent by email. This signal may be used to validate that
the submit date stored in the URL is no older than a certain time. If any
receiver returns False the process is discarded and the user receives a
discarded message.
"""
