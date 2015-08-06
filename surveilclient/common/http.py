# Copyright 2012 OpenStack Foundation
# Copyright 2014 - Savoir-Faire Linux inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import requests
import requests.exceptions

from surveilclient import exc
from surveilclient.openstack.common.py3kcompat import urlutils

import copy
import json
import time


USER_AGENT = 'python-surveilclient'


class HTTPClient(object):

    def __init__(self,
                 endpoint,
                 username=None,
                 password=None,
                 tenant_name=None,
                 auth_url=None,
                 authenticated=True):
        endpoint_parts = urlutils.urlparse(endpoint)
        self.endpoint_hostname = endpoint_parts.hostname
        self.endpoint_port = endpoint_parts.port
        self.endpoint_path = endpoint_parts.path

        self.authenticated = authenticated
        if self.authenticated:
            self.auth_username = username
            self.auth_password = password
            self.tenant_name = tenant_name
            self.auth_url = auth_url
            self.auth_token = {}

    def _token_valid(self):
        if self.auth_token.get('id', None) is None:
            return False
        #  TODO(aviau): Check expiration date on token.
        return True

    def _get_auth_token(self):
        """Returns an auth token."""

        if self._token_valid():
            return self.auth_token['id']

        auth_url = self.auth_url + '/tokens'
        credentials = {}

        resp = None
        for attempt in range(3):
            try:
                resp = requests.post(auth_url, data=json.dumps(credentials))
                break
            except requests.exceptions.ConnectionError as exp:
                if attempt == 2:
                    raise exp
                time.sleep(1)

        access = resp.json()
        self.auth_token = access['access']['token']
        return self.auth_token['id']

    def _create_complete_url(self, url):
        # TODO(aviau): https
        return ('http://' + self.endpoint_hostname + ":"
                + str(self.endpoint_port) + self.endpoint_path + url)

    def _http_request(self, url, method, **kwargs):
        """Send an http request with the specified characteristics.

        Wrapper around requests to handle tasks such
        as setting headers and error handling.
        """
        kwargs['headers'] = copy.deepcopy(kwargs.get('headers', {}))
        kwargs['headers'].setdefault('User-Agent', USER_AGENT)

        if self.authenticated:
            kwargs['headers']['X-Auth-Token'] = self._get_auth_token()

        url = self._create_complete_url(url)
        for attempt in range(3):
            try:
                resp = getattr(requests, method.lower())(url, **kwargs)
                break
            except (
                    requests.Timeout,
                    requests.ConnectionError
            ) as exp:
                if attempt == 2:
                    raise exp
                time.sleep(1)

        if 400 <= resp.status_code < 600:
            raise exc.from_response(
                response=resp, body=resp.content, method=method, url=url)
        elif resp.status_code == 300:
            raise exc.from_response(
                response=resp, body=resp.content, method=method, url=url)

        return resp

    def json_request(self, url, method, **kwargs):
        """Send an http request with the specified characteristics.

        """
        kwargs['headers'] = copy.deepcopy(kwargs.get('headers', {}))
        kwargs['headers'].setdefault('Content-Type', 'application/json')

        if 'data' in kwargs:
            kwargs['data'] = json.dumps(kwargs['data'])

        resp, content = self.request(url, method, **kwargs)
        return resp, resp.json() if content != '' else ''

    def request(self, url, method, **kwargs):
        """Send an http request with the specified characteristics.

        """
        kwargs['headers'] = copy.deepcopy(kwargs.get('headers', {}))

        resp = self._http_request(url, method, **kwargs)
        return resp, resp.content.decode()
