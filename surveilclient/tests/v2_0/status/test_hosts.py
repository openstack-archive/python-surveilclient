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


class TestHosts(clienttest.ClientTest):

    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:8080/v2/status/hosts",
            body='[{"host_name": "host1"}]'
        )

        hosts = self.client.status.hosts.list()

        self.assertEqual(
            hosts,
            [{"host_name": "host1"}]
        )

    @httpretty.activate
    def test_get(self):
        httpretty.register_uri(
            httpretty.GET, "http://localhost:8080/v2/status/hosts/hostname",
            body='{"host_name": "host1"}'
        )

        host = self.client.status.hosts.get("hostname")

        self.assertEqual(
            host,
            {"host_name": "host1"}
        )

    @httpretty.activate
    def test_submit_host_check_result(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:8080/v2/status/hosts/localhost"
                            "/results",
            body=''
        )

        self.client.status.hosts.submit_check_result(
            "localhost", output="someoutput"
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {"output": u"someoutput"}
        )