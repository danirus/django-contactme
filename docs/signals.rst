.. _ref-signals:

=======
Signals
=======

List of signals sent by the django-contactme app.

Confirmation will be requested
==============================

**django_contactme.signals.confirmation_will_be_requested**
    Sent just before a confirmation message is requested.

    A message is sent to the user right after the contact form is been posted and validated to verify the user's email address. This signal may be used to ban email addresses or check message content. If any receiver returns False the process is discarded and the user receives a discarded message.


Confirmation has been requested
===============================

**django_contactme.signals.confirmation_requested**
    Sent just after a confirmation message is requested.

    A message is sent to the user right after the contact form is been posted and validated to verify the user's email address. This signal may be uses to trace contact messages posted but never confirmed.


Confirmation has been received
==============================

**django_contactme.signals.confirmation_received**
    Sent just after a confirmation has been received.

    A confirmation is received when the user clicks on the link provided in the confirmation message sent by email. This signal may be used to validate that the submit date stored in the URL is no older than a certain time. If any receiver returns False the process is discarded and the user receives a discarded message. 

    See a simple example of a receiver for this signal: :ref:`signals-and-receivers-label`, in the Tutorial.
