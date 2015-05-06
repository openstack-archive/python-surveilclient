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

import httpretty

from surveilclient.tests.v2_0 import clienttest


class TestHosts(clienttest.ClientTest):

    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.GET, "http://localhost:8080/v2/config/hosts",
            body='[{"host_name": "host1"}]'
        )

        hosts = self.client.config.hosts.list()

        self.assertEqual(
            hosts,
            [{u"host_name": u"host1"}]
        )

    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:8080/v2/config/hosts",
            body='{"host_name": "new_host"}'
        )

        self.client.config.hosts.create(
            host_name="new_host"
        )

        self.assertEqual(
            httpretty.last_request().body.decode(),
            u'{"host_name": "new_host"}'
        )

    @httpretty.activate
    def test_delete(self):
        httpretty.register_uri(
            httpretty.DELETE,
            "http://localhost:8080/v2/config/hosts/host_name_to_delete",
            body="body"
        )

        body = self.client.config.hosts.delete(
            host_name="host_name_to_delete",
        )

        self.assertEqual(
            body,
            "body"
        )