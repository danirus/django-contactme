import os
import sys
from setuptools import setup, find_packages


setup_dict = {
    'name': 'django-contactme',
    'version': '1.3.0',
    'packages': find_packages(),
    'license': 'MIT',
    'description': 'Django pluggable contact form app with email verification.',
    'long_description': ("A reusable Django app that adds a contact form "
			 "with email protection to your site. Contact data "
			 "will only hit the database when users confirm "
			 "their email address after submitting the form."),
    'author': 'Daniel Rus Morales',
    'author_email': 'mbox@danir.us',
    'maintainer': 'Daniel Rus Morales',
    'maintainer_email': 'mbox@danir.us',
    'url': 'http://github.com/danirus/django-contactme/',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
    'include_package_data': True,
    'install_requires': ['Django>=1.8'],
}

setup(**setup_dict)
