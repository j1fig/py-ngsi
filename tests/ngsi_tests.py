from unittest import TestCase

from ngsi import Client


class NgsiClientTests(TestCase):
    def setUp(self):
        self.test_host = '130.206.117.120'

    def test_version(self):
        c = Client(host=self.test_host)
        self.assertEqual(c.version()['version'], '0.19.0')
