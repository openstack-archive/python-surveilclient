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

import requests_mock

from surveilclient.tests.v2_0 import clienttest


class TestCheckModulations(clienttest.ClientTest):
    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/checkmodulations",
                  text='{"message": "Ack received!"}')

            self.client.config.checkmodulations.create(
                check_command='test',
                check_period='test',
                checkmodulation_name='test'
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {"checkmodulation_name": "test",
                 "check_command": "test",
                 "check_period": "test"}
            )

    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/checkmodulations",
                   text='[{"checkmodulation_name": "test",'
                        '"check_command": "test",'
                        '"check_period": "test"}]'
                   )

            self.assertEqual(
                self.client.config.checkmodulations.list(),
                [{"checkmodulation_name": "test",
                  "check_command": "test", "check_period": "test"}]
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/"
                     "checkmodulations/checkmodulation_to_delete",
                     text='body')

            body = self.client.config.checkmodulations.delete(
                checkmodulation_name='checkmodulation_to_delete'
            )

            self.assertEqual(
                body,
                "body"
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get('http://localhost:5311/v2/config/checkmodulations/' +
                  'ping_night',
                  text='{"checkmodulation_name": "ping_night",'
                       '"check_command": "check_ping_night",'
                       '"check_period": "night"}'
                  )

            checkmodulation = self.client.config.checkmodulations.get(
                checkmodulation_name='ping_night'
            )

            self.assertEqual(
                checkmodulation,
                {"checkmodulation_name": "ping_night",
                 "check_command": "check_ping_night",
                 "check_period": "night"}
            )

    def test_update(self):
        with requests_mock.mock() as m:
            m.put('http://localhost:5311/v2/config/checkmodulations/' +
                  'ping_night',
                  text='{"check_command": "updated"}')

            self.client.config.checkmodulations.update(
                checkmodulation_name='ping_night',
                checkmodulation={"check_command": "updated"}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "check_command": u"updated"
                }
            )
