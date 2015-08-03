from unittest import TestCase
from datetime import timedelta

from ngsi import Client


class NgsiClientTests(TestCase):
    def setUp(self):
        self.test_host = '127.0.0.1'
        self.test_elements = [
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
            }
        ]
        self.test_entities = [
            {
                "type": "Room",
                "isPattern": "false",
                "id": "Room1"
            }
        ]
        self.test_reference = 'http://requestb.in/1g22in51'
        self.test_attributes = ["temperature"]
        self.test_duration = timedelta(days=30)
        self.test_notify_conditions = [
            {
                "type": "ONTIMEINTERVAL",
                "condValues": [
                    "PT10S"
                ]
            }
        ]

    def test_version(self):
        c = Client(host=self.test_host)
        self.assertEqual(c.version()['version'], '0.22.0-next')

    def test_create_context(self):
        c = Client(host=self.test_host)
        r = c.create_context(self.test_elements)
        for element in r:
            self.assertEqual(element['statusCode']['code'], '200')

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
            self.assertEqual(element['statusCode']['code'], '200')

    def test_subscribe_context(self):
        c = Client(host=self.test_host)
        r = c.subscribe_context(
            entities=self.test_entities,
            callback_url=self.test_reference,
            duration=self.test_duration,
            notification_type=self.test_notify_conditions,
            attributes=self.test_attributes
        )

        self.assertTrue('subscriptionId' in r)

    def test_update_subscribe_context(self):
        test_update_notify_conditions = [
            {
                "type": "ONTIMEINTERVAL",
                "condValues": [
                    "PT15S"
                ]
            }
        ]

        c = Client(host=self.test_host)
        r = c.subscribe_context(
            entities=self.test_entities,
            callback_url=self.test_reference,
            duration=self.test_duration,
            notification_type=self.test_notify_conditions,
            attributes=self.test_attributes
        )
        sub_id = r['subscriptionId']

        r = c.update_context_subscription(
            sub_id,
            notifyConditions=test_update_notify_conditions
        )
        self.assertEqual(r['subscriptionId'], sub_id)

        r = c.unsubscribe_context(sub_id)

    def test_unsubscribe_context(self):
        c = Client(host=self.test_host)
        r = c.subscribe_context(
            entities=self.test_entities,
            callback_url=self.test_reference,
            duration=self.test_duration,
            notification_type=self.test_notify_conditions,
            attributes=self.test_attributes
        )
        sub_id = r['subscriptionId']

        r = c.unsubscribe_context(sub_id)

        self.assertEqual(r['statusCode']['code'], '200')
