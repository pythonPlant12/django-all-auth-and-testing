from django.test import TestCase
import os


class TryDjangoConfigTest(TestCase):
    def test_config(self):
        self.assertNotEqual(None,
                         os.environ.get("DJANGO_SECRET_KEY"))
