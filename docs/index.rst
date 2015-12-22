.. django-contactme documentation master file, created by
   sphinx-quickstart on Sat Dec 10 00:09:54 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


==============================
django-contactme documentation
==============================

**django-contactme** provides a simple contact form that only hits the database when the user has visited the confirmation URL. Emails are threaded to avoid response blocking. It comes with a complete unittest set for both the backend functionality and the Jquery plugin.

Version 1.3 is compatible with:

 * Django 1.9 under Python 2.7, 3.4, 3.5
 * Django 1.8 under Python 2.7, 3.4, 3.5

Version 1.2 is compatible with:

 * Django 1.8 under Python 2.7, 3.4
 * Django 1.7 under Python 2.7, 3.4
 * Django 1.6 under Python 2.7, 3.4
 * Django 1.5 under Python 2.7, 3.4
 * Django 1.4 under PYthon 2.7

Table of contents:

.. toctree::
   :maxdepth: 2

   example
   tutorial
   signals
   templatetags
   settings
   templates


Quick start
===========

1. Add ``django_contactme`` to ``INSTALLED_APPS``.
2. Add ``url(r'^contact/', include('django_contactme.urls'))`` to your root URLconf.
3. Run the ``migrate`` command to apply migrations.
4. Run the ``runserver`` command and check the new contact form at http://localhost:8000/contact/


Workflow in short
=================

The user...

1. Clicks on the `contact me/us` link of your site.

2. Fills in the contact form data with her ``name``, ``email address`` and ``message``, and clicks on `preview`.

3. She finally clicks on `post` and submit the form.

4. Then django-contactme:
   
  * Creates a token with the contact form data.

  * Sends an email to the user with a confirmation URL containing the token.

  * And shows a template informing the user that she must click on the link to confirm the message.

5. The user receives the email, opens it, and clicks on the confirmation link.

6. Then django-contactme:
   
  * Verifies the token and creates a ``ContactMsg`` model instance.

  * Sends an email to the addresses listed in :ref:`ref-CONTACTME-NOTIFY-TO`, to notify that a new contact message has reached the database.

  * And finally shows a template being grateful for the message.

Read a longer workflow description in the :ref:`workflow-label` section of the Tutorial.
