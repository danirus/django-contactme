import os
import sys


def setup_django_settings():
    if os.environ.get("DJANGO_SETTINGS_MODULE", False):
        return
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, os.getcwd())
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
