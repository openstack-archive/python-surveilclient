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

import requests_mock

from surveilclient.tests.v2_0 import clienttest


class TestHosts(clienttest.ClientTest):

    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/hosts",
                   text='[{"host_name": "host1"}]')

            hosts = self.client.config.hosts.list()

            self.assertEqual(
                hosts,
                [{u"host_name": u"host1"}]
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "filters": '{"isnot": {"register": ["0"]}}'
                }
            )

    def test_list_templates(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/hosts",
                   text='[]')

            self.client.config.hosts.list(templates=True)
            self.assertEqual(
                m.last_request.path,
                '/v2/config/hosts'
            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/hosts",
                  text='{"host_name": "new_host", "address": "192.168.2.1"}')

            self.client.config.hosts.create(
                host_name="new_host",
                address="192.168.2.1"
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "host_name": "new_host",
                    "address": "192.168.2.1"
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get("http://localhost:5311/v2/config/hosts/host_name_to_show",
                  text='{"host_name": "host_name_to_show"}')

            host = self.client.config.hosts.get(
                host_name="host_name_to_show"
            )

            self.assertEqual(
                host,
                {"host_name": "host_name_to_show"}
            )

    def test_update(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/hosts/host_name_to_update",
                  text='{"test": "test"}')

            self.client.config.hosts.update(
                host_name="host_name_to_update",
                host={'address': "192.168.0.1",
                      'check_period': "24x7"
                      }
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "check_period": u"24x7",
                    "address": u"192.168.0.1"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/"
                     "config/hosts/host_name_to_delete",
                     text="body")

            body = self.client.config.hosts.delete(
                host_name="host_name_to_delete",
            )

            self.assertEqual(
                body,
                "body"
            )
