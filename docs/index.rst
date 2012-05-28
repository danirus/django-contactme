.. django-contactme documentation master file, created by
   sphinx-quickstart on Sat Dec 10 00:09:54 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============

**Django-contactme** provides a simple contact form that only hits the database 
after the user confirm her email address. Emails are threaded to avoid response blocking.


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
3. ``syncdb``, ``runserver``, and
4. Hit http://localhost:8000/contact/ in your browser!


Workflow in short
=================

The user...

#. Clicks on the `contact me/us` link of your site.

#. She fills in the contact form data with her ``name``, ``email address`` and ``message``, and clicks on `preview`.

#. She finally clicks on `post` and submit the form.

#. Then Django-ContactMe:

 #. Creates a token with the contact form data.

 #. Sends an email to her with a confirmation URL containing the token.

 #. And shows a template telling her she must click on the link to confirm the message.

#. She receives the email, she opens it, and she clicks on the confirmation link.

#. Then Django-ContactMe:

 #. Check that the token is correct and creates a ``ContactMsg`` model instance.

 #. Sends an email to ``CONTACTME_NOTIFY_TO`` addresses notifying that a new contact message has arrived.

 #. And shows a template being grateful to her for the message.

Read a longer workflow description in the :ref:`workflow-label` section of the Tutorial.
