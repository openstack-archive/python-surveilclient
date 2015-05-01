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

import json
import unittest

import httpretty

from surveilclient.common import http


class TestHttp(unittest.TestCase):

    def setUp(self):
        self.surveil_url = 'http://surveil:8080/v1'
        self.client = http.HTTPClient(self.surveil_url, authenticated=False)

    @httpretty.activate
    def test_json_request_get(self):
        example_result = {'hello': 'surveil'}
        httpretty.register_uri(httpretty.GET,
                               self.surveil_url + "/test",
                               body=json.dumps(example_result))

        resp, body = self.client.json_request('/test', 'GET')
        self.assertEqual(httpretty.last_request().method, 'GET')
        self.assertEqual(body, example_result)

        self.assertEqual(
            httpretty.last_request().headers['Content-Type'],
            'application/json'
        )
