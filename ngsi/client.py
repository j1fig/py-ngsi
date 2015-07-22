from uuid import uuid4
import requests


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

    def _update_context(self, elements, action=None):
        data = {}
        data['contextElements'] = elements
        if action:
            data['updateAction'] = action
        response = self._call_api(method='post', url='updateContext', json=data)
        return response.json()['contextResponses']

    def _call_api(self, method, url, params=None, json=None):
        """
        A simple wrapper around host requests
        """
        return requests.request(
            method,
            self._api_url_v1+url,
            params=params,
            headers=self._headers,
            json=json
        )
