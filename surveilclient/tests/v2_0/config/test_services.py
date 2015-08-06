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


class TestServices(clienttest.ClientTest):

    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/services",
                   text='[{"service_name": "service1"}]')

            services = self.client.config.services.list()

            self.assertEqual(
                services,
                [{"service_name": "service1"}]
            )
            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "filters": '{"isnot": {"register": ["0"]}}'
                }
            )

    def test_list_templates(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/services",
                   text='[{"service_name": "service1"}]')

            self.client.config.services.list(templates=True)
            self.assertEqual(
                m.last_request.path,
                '/v2/config/services'
            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/services",
                  text='{"service_name": "new_service"}')

            self.client.config.services.create(
                service_name="new_service"
            )

            self.assertEqual(
                m.last_request.body,
                '{"service_name": "new_service"}'
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/hosts/host_name/" +
                     "services/service_description",
                     text="body")

            body = self.client.config.services.delete(
                host_name="host_name",
                service_description="service_description"
            )

        self.assertEqual(
            body,
            "body"
        )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get("http://localhost:5311/v2/config/hosts/host_name/" +
                  "services/service_description",
                  text="{}")

            body = self.client.config.services.get(
                host_name="host_name",
                service_description="service_description"
            )

            self.assertEqual(
                body,
                {}
            )
