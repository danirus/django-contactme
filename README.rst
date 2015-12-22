django-contactme
================

|pypi| |travis| |coveralls|

.. |travis| image:: https://secure.travis-ci.org/danirus/django-contactme.png?branch=master
    :target: https://travis-ci.org/danirus/django-contactme
.. |pypi| image:: https://badge.fury.io/py/django-contactme.png
    :target: http://badge.fury.io/py/django-contactme
.. |coveralls| image:: https://coveralls.io/repos/danirus/django-contactme/badge.png?branch=master
    :target: https://coveralls.io/r/danirus/django-contactme?branch=master


Simple and stable Django app that provides a contact form with email protection:
1. Contact data only hit the database when the user confirms the verification URL sent by email
2. Emails are threaded to avoid response blocking
3. Supports Django 1.8 and 1.9 under Python 2.7, 3.4 and 3.5

Read the documentation at:

* `Read The Docs`_
* `Python Packages Site`_

.. _`Read The Docs`: http://readthedocs.org/docs/django-contactme/
.. _`Python Packages Site`: http://packages.python.org/django-contactme/

Includes several **demo sites** and a complete **test suite** for the backend code and the jquery plugin.
