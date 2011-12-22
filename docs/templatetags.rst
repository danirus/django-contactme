.. _ref-templatetags:

============
Templatetags
============

Django-contactme has a templatetag to render the contact form.

``render_contact_form``
=======================

Many sites use a hidden div that fadeIn/slideUp when the user clicks on the **contact me/us** link. Use ``render_contact_form`` templatetag to render the contact form anywhere in your template. It uses the ``django_contactme/form.html`` template to render the form.
