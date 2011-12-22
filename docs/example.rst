.. _ref-example:

============
Demo prpject
============

Django-contactme comes with a demo project to see the app in action.


Demo quick setup
================

1. ``cd`` into the ``demo`` directory
2. ``python manage syncdb`` will create a simple SQLite db file for the demo.
3. Run the server ``python manage runserver`` and browse http://localhost:8000


Email settings
==============

By default the demo project send email messages to the standard output. You can customize a few email settings to allow Django sending emails. This will allow you to receive email messages with confirmation URLs that actually work.

Edit the ``demo/settings.py`` file, go to the end of the file and customize the following settings. Provide actual values of your email address and email provider::

    EMAIL_HOST          = "" # gmail: "smtp.gmail.com"
    EMAIL_PORT          = "" # gmail: "587"
    EMAIL_HOST_USER     = "" # gmail: user@gmail.com
    EMAIL_HOST_PASSWORD = ""
    EMAIL_USE_TLS       = True # gmail

    DEFAULT_FROM_EMAIL  = "Your site name <user@gmail.com>"
    SERVER_EMAIL        = DEFAULT_FROM_EMAIL

    # Fill in actual EMAIL settings above, and comment out the 
    # following line to let the django demo sending actual emails
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    CONTACTME_NOTIFY_TO = "Your name <user@gmail.com>"


The domain used in the links sent by email refers to `example.com` and thus are not associated with your django development web server. Enter in the admin UI and change the domain name to something like `localhost:8000`.


Register a signal receiver
==========================

After trying the demo site you may like to add a receiver for any of the signals sent during the workflow.

Read the :doc:`signals` to know more about Django-ContactMe signals.

Read the :ref:`signals-and-receivers-label` in the Tutorial to see an example.
