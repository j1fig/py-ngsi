import json
import requests


class Client(object):
    def __init__(self, host, port=1026):
        self.host = host
        self.port = port
        self.base_url = 'http://' + str(self.host) + ':' + str(self.port) + '/'
        self._headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }

    def version(self):
        """
        Returns context broker version
        """
        response = self._get('version')
        return json.loads(response.content)['orion']

    def _get(self, url, params=None):
        """
        A simple wrapper around host GET requests
        """
        return requests.get(
            self.base_url+url,
            params=params,
            headers=self._headers
        )
