import os
import sys
import unittest


def setup_django_settings():
    os.chdir(os.path.join(os.path.dirname(__file__), "..", ".."))
    sys.path.insert(0, os.getcwd())
    os.environ["DJANGO_SETTINGS_MODULE"] = "django_contactme.tests.settings"


def run_tests():
    if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
        setup_django_settings()

    from django.conf import settings
    from django.test.utils import get_runner

    runner = get_runner(settings, "django.test.simple.DjangoTestSuiteRunner")
    test_suite = runner(verbosity=2, interactive=True, failfast=False)
    test_suite.run_tests(["django_contactme"])


def suite():
    if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
        setup_django_settings()

    from django_contactme.tests import forms, views

    testsuite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromModule(views),
        unittest.TestLoader().loadTestsFromModule(forms),
    ])
    return testsuite


if __name__ == "__main__":
    run_tests()
