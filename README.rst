django-contactme
================

|downloads|_ |TravisCI|_

.. |TravisCI| image:: https://secure.travis-ci.org/danirus/django-contactme.png?branch=master
.. _TravisCI: https://travis-ci.org/danirus/django-contactme
.. |downloads| image:: https://pypip.in/d/django-contactme/badge.png
        :target: https://pypi.python.org/pypi/django-contactme
.. _downloads: https://pypi.python.org/pypi/django-contactme

Tested under:

* Python 3.2 and django 1.5.1: `builds <http://buildbot.danir.us/builders/django-contactme-py32dj15>`_
* Python 2.7 and django 1.5.1: `builds <http://buildbot.danir.us/builders/django-contactme-py27dj15>`_
* Python 2.7 and django 1.4.5: `builds <http://buildbot.danir.us/builders/django-contactme-py27dj14>`_

By Daniel Rus Morales <http://danir.us/>

* http://pypi.python.org/pypi/django-contactme/
* http://github.com/danirus/django-contactme/

A reusable Django app that adds a contact form with email protection to your site:
1. Contact data only hit the database when the user confirms her email address
2. Emails are threaded to avoid response blocking

Read the documentation at:

* `Read The Docs`_
* `Python Packages Site`_

.. _`Read The Docs`: http://readthedocs.org/docs/django-contactme/
.. _`Python Packages Site`: http://packages.python.org/django-contactme/

Includes a **demo site** limited **test suite**. If you commit code, please consider adding proper coverage (especially if it has a chance for a regression) in the test suite.

Run the tests with: ``python setup.py test``
