import sys
from setuptools import setup, find_packages
from setuptools.command.test import test

def run_tests(*args):
    from django_contactme.tests import run_tests
    errors = run_tests()
    if errors:
        sys.exit(1)
    else:
        sys.exit(0)

test.run_tests = run_tests

setup(
    name = "django-contactme",
    version = "1.1a1",
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
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    test_suite = "dummy",
    include_package_data=True,
)
