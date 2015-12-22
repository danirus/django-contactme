.. _ref-example:

=============
Demo projects
=============

The source package of django-contactme comes with several demo projects to see the application in action:

 * **bare_demo** is the simplest demo possible.
 * **bare_demo_with_ajax** is the same previous example plus Ajax functionality provided by ``jquery.djcontactme.js``, the jquery plugin that comes with the application.
 * **crispy_forms_demo** is an example of how to use django-contactme with `django-crispy-forms <http://django-crispy-forms.readthedocs.org/en/latest/>`_.


Demo quick setup
================

Demo projects live inside the ``example`` project in app's root directory.

The simplest and less interfeing way to run the demo projects is by creating a virtualenv for django-contactme. Then:

1. ``cd`` into the any of the demo directories.
2. Run ``python manage migrate`` to create a minimal SQLite db for the demo.
3. Run ``python manage runserver`` and browse http://localhost:8000

In addition, **crispy_forms_demo** requires the **crispy_forms** package::

  $ pip install django-crispy-forms
  

Email settings
==============

By default the demo project send email messages to the standard output. You can customize the email settings to send actual emails.

Edit the ``settings.py`` module, go to the end of the file and customize the following entries::

    EMAIL_HOST          = "" # for gmail it would be: "smtp.gmail.com"
    EMAIL_PORT          = "" # for gmail: "587"
    EMAIL_HOST_USER     = "" # for gmail: user@gmail.com
    EMAIL_HOST_PASSWORD = ""
    EMAIL_USE_TLS       = True # for gmail

    DEFAULT_FROM_EMAIL  = "Your site name <user@gmail.com>"
    SERVER_EMAIL        = DEFAULT_FROM_EMAIL

    # Fill in actual EMAIL settings above, and comment out the 
    # following line to let the django demo sending actual emails
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    CONTACTME_NOTIFY_TO = "Your name <user@gmail.com>"


The domain used in the links sent by email refers to `example.com` and thus are not associated with your django development web server. Change the domain name through the admin interface, sites application, to something like `localhost:8000` so that URLs in email messages match your development server.


Register a signal receiver
==========================

After trying the demo site you may like to add a receiver for any of the signals sent during the workflow.

Read the entry on :doc:`signals` to know more about django-contactme signals. The section :ref:`signals-and-receivers-label` in the Tutorial shows a use case.
