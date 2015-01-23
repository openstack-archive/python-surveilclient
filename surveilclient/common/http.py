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

from six.moves import http_client as httplib

from surveilclient import exc
from surveilclient.openstack.common.py3kcompat import urlutils

import copy
import json


USER_AGENT = 'python-surveilclient'


class HTTPClient(object):

    def __init__(self, endpoint):
        endpoint_parts = urlutils.urlparse(endpoint)
        self.endpoint_hostname = endpoint_parts.hostname
        self.endpoint_port = endpoint_parts.port
        self.endpoint_path = endpoint_parts.path

    def get_connection(self):
        # TODO(aviau): https
        con = httplib.HTTPConnection(
            self.endpoint_hostname,
            self.endpoint_port
        )

        return con

    def _http_request(self, url, method, **kwargs):
        """Send an http request with the specified characteristics.

        Wrapper around httplib.HTTP(S)Connection.request to handle tasks such
        as setting headers and error handling.
        """
        kwargs['headers'] = copy.deepcopy(kwargs.get('headers', {}))
        kwargs['headers'].setdefault('User-Agent', USER_AGENT)
        conn = self.get_connection()
        conn.request(method, self.endpoint_path + url, **kwargs)
        resp = conn.getresponse()

        body_str = resp.read()

        if 400 <= resp.status < 600:
            raise exc.from_response(
                response=resp, body=body_str, method=method, url=url)
        elif resp.status == 300:
            raise exc.from_response(
                response=resp, body=body_str, method=method, url=url)

        return resp, body_str

    def json_request(self, url, method, **kwargs):
        """Send an http request with the specified characteristics.

        """
        kwargs['headers'] = copy.deepcopy(kwargs.get('headers', {}))
        kwargs['headers'].setdefault('Content-Type', 'application/json')

        if 'body' in kwargs:
            kwargs['body'] = json.dumps(kwargs['body'])

        resp, body = self._http_request(url, method, **kwargs)
        return resp, json.loads(body.decode())
