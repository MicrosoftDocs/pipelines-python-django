from django.test import TestCase

class HelloWorldTest(TestCase):
    def test_site(self):
        self.assertEqual(1, 1)