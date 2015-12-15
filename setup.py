import sys
from setuptools import setup, find_packages
from setuptools.command.test import test

class TestCommand(test):
    def run(self):
        import django, pytest
        from django_contactme.tests import setup_django_settings
        setup_django_settings()
        django.setup()
        pytest.main(['-v',])

setup(
    name = "django-contactme",
    version = "1.3.0",
    packages = find_packages(),
    license = "MIT",
    description = "Django pluggable contact form app with email verification.",
    long_description = "A reusable Django app that adds a contact form with email protection to your site. Contact data will only hit the database when users confirm their email address after submitting the form.",
    author = "Daniel Rus Morales",
    author_email = "inbox@danir.us",
    maintainer = "Daniel Rus Morales",
    maintainer_email = "inbox@danir.us",
    url = "http://github.com/danirus/django-contactme/",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
    include_package_data=True,
    cmdclass={'test': TestCommand},
)
