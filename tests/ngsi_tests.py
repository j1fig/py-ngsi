from unittest import TestCase

from ngsi import Client


class NgsiClientTests(TestCase):
    def setUp(self):
        self.test_host = '130.206.117.120'

    def test_version(self):
        c = Client(host=self.test_host)
        self.assertEqual(c.version()['version'], '0.19.0')

    def test_create_context(self):
        test_elements = [
        {
            "type": "Room",
            "isPattern": "false",
            "id": "Room3",
            "attributes": [
                {
                "name": "temperature",
                "type": "float",
                "value": "23"
                },
                {
                "name": "pressure",
                "type": "integer",
                "value": "720"
                }
            ]
        },
        {
            "type": "Room",
            "isPattern": "false",
            "id": "Room4",
            "attributes": [
                {
                "name": "temperature",
                "type": "float",
                "value": "33"
                },
                {
                "name": "pressure",
                "type": "integer",
                "value": "1100"
                }
            ]
        }]

        c = Client(host=self.test_host)
        r = c.create_context(test_elements)
        for element in r:
            self.assertEqual(element['statusCode']['code'],'200')

    def test_get_context(self):
        test_entities = [
            {
                "type": "Room",
                "isPattern": "true",
                "id": "Room*"
            }
        ]

        c = Client(host=self.test_host)
        r = c.get_context(test_entities)
        for element in r:
            self.assertEqual(element['statusCode']['code'],'200')
