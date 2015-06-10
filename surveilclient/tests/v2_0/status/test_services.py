# Copyright 2015 - Savoir-Faire Linux inc.
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

import httpretty

from surveilclient.tests.v2_0 import clienttest


class TestServices(clienttest.ClientTest):

    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:8080/v2/status/services",
            body='[{"service_name": "service1"}]'
        )

        services = self.client.status.services.list()

        self.assertEqual(
            services,
            [{"service_name": "service1"}]
        )

    @httpretty.activate
    def test_submit_service_check_result(self):
        httpretty.register_uri(
            httpretty.POST,
            "http://localhost:8080/v2/status/hosts/localhost"
            "/services/testservice/results",
            body=''
        )

        self.client.status.services.submit_check_result(
            "localhost",
            'testservice',
            output="someoutputt"
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {"output": u"someoutputt"}
        )
