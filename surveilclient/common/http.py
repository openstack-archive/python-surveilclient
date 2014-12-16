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

import copy
import httplib
import json
import urlparse


class HTTPClient(object):

    def __init__(self, endpoint):
        endpoint_parts = urlparse.urlparse(endpoint)
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

    def json_request(self, url, method, **kwargs):
        """Send an http request with the specified characteristics.

        """
        conn = self.get_connection()

        kwargs['headers'] = copy.deepcopy(kwargs.get('headers', {}))
        kwargs['headers'].setdefault('Content-Type', 'application/json')

        conn.request(
            method,
            self.endpoint_path + url,
            headers=kwargs['headers']
        )

        resp = conn.getresponse()
        return json.loads(resp.read())
