django-contactme
================

|pypi| |travis| |coveralls|

.. |travis| image:: https://secure.travis-ci.org/danirus/django-contactme.png?branch=master
    :target: https://travis-ci.org/danirus/django-contactme
.. |pypi| image:: https://badge.fury.io/py/django-contactme.png
    :target: http://badge.fury.io/py/django-contactme
.. |coveralls| image:: https://coveralls.io/repos/danirus/django-contactme/badge.png?branch=master
    :target: https://coveralls.io/r/danirus/django-contactme?branch=master


A reusable Django app that adds a contact form with email protection to your site:
1. Contact data only hit the database when the user confirms her email address
2. Emails are threaded to avoid response blocking
3. Support Django 1.4, 1.5, 1.6, 1.7 and 1.8
4. Python 3 for Django 1.5, 1.6, 1.7, 1.8

Read the documentation at:

* `Read The Docs`_
* `Python Packages Site`_

.. _`Read The Docs`: http://readthedocs.org/docs/django-contactme/
.. _`Python Packages Site`: http://packages.python.org/django-contactme/

Includes a **demo site** limited **test suite**. If you commit code, please consider adding proper coverage (especially if it has a chance for a regression) in the test suite.

Run the tests with: ``tox``.
