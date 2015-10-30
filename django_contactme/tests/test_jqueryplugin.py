from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

try:
    from django.contrib.staticfiles.testing import StaticLiveServerTestCase
except ImportError:
    StaticLiveServerTestCase = None
from django.core.urlresolvers import reverse

if StaticLiveServerTestCase:
    class QunitTests(StaticLiveServerTestCase):

        @classmethod
        def setUpClass(cls):
            cls.browser = webdriver.PhantomJS()
            super(QunitTests, cls).setUpClass()

        @classmethod
        def tearDownClass(cls):
            cls.browser.quit()
            super(QunitTests, cls).tearDownClass()

        def test_jqueryplugin_with_qunit(self):
            url = "%s%s" % (self.live_server_url, reverse('qunit-tests'))
            self.browser.implicitly_wait(1)
            self.browser.get(url)
            results = WebDriverWait(self.browser, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, 'qunit-testresult')))
            self.browser.save_screenshot('/Users/danirus/screenshot.png')
            total = int(results.find_element_by_class_name('total').text)
            failed = int(results.find_element_by_class_name('failed').text)
            self.assertTrue(total and not failed, results.text)
