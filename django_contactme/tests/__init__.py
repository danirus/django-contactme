import unittest


def suite():
    from django_contactme.tests import test_forms, test_views

    testsuite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromModule(test_views),
        unittest.TestLoader().loadTestsFromModule(test_forms),
    ])
    return testsuite
