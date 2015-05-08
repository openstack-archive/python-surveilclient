# Copyright 2015 - Savoir-Faire Linux inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import json

import httpretty

from surveilclient.tests.v2_0 import clienttest


class TestCheckModulations(clienttest.ClientTest):
    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:8080/v2/config/checkmodulations",
            body='{"message": "Ack received!"}')

        self.client.config.checkmodulations.create(
            check_command='test',
            check_period='test',
            checkmodulation_name='test'
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {"checkmodulation_name": "test",
             "check_command": "test",
             "check_period": "test"}
        )

    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.GET, "http://localhost:8080/v2/config/checkmodulations",
            body='[{"checkmodulation_name": "test","check_command": "test",'
                 '"check_period": "test"}]'
            )

        self.assertEqual(
            self.client.config.checkmodulations.list(),
            [{"checkmodulation_name": "test",
              "check_command": "test", "check_period": "test"}]
        )

    @httpretty.activate
    def test_delete(self):
        httpretty.register_uri(
            httpretty.DELETE, "http://localhost:8080/v2/config/"
                              "checkmodulations/checkmodulation_to_delete",
            body='body')

        body = self.client.config.checkmodulations.delete(
            checkmodulation_name='checkmodulation_to_delete'
        )

        self.assertEqual(
            body,
            "body"
        )