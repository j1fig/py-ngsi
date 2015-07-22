from uuid import uuid4
import requests

from ngsi.models import QueryError

class Client(object):
    def __init__(self, host, port=1026):
        self.host = host
        self.port = port
        self._base_url = \
            'http://' + str(self.host) + ':' + str(self.port) + '/'
        self._headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }
        self._api_url_v1 = self._base_url + 'v1/'

    def version(self):
        """
        Returns context broker version
        """
        response = requests.get(
            self._base_url + 'version',
            headers=self._headers)
        return response.json()['orion']

    def create_context(self, elements):
        return self._update_context(elements, action='APPEND')

    def get_context(self, entities, attributes=None):
        return self._query_context(entities, attributes)

    def _update_context(self, elements, action=None):
        data = {}
        data['contextElements'] = elements
        if action:
            data['updateAction'] = action
        response = self._call_api(method='post', url='updateContext', json=data)
        return response.json()['contextResponses']

    def _query_context(self, entities, attributes=None):
        data = {}
        data['entities'] = entities
        if attributes:
            data['attributes'] = attributes
        response = self._call_api(method='post', url='queryContext', json=data)
        json_response = response.json()
        if 'contextResponses' in json_response:
            return json_response['contextResponses']
        elif 'errorCode' in json_response:
            error = json_response['errorCode']
            raise QueryError('Error code ' +
                             error['code'] + ': ' +
                             error['reasonPhrase'])
        return response.json()['contextResponses']

    def _call_api(self, method, url, params=None, json=None):
        """
        A simple wrapper around host requests
        """
        response = requests.request(
            method,
            self._api_url_v1+url,
            params=params,
            headers=self._headers,
            json=json
        )
        response.raise_for_status()
        return response
