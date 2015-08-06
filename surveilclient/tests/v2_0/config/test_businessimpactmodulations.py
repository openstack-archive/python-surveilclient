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


class TestBusinessImpactModulations(clienttest.ClientTest):
    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/"
                   "businessimpactmodulations",
                   text='[{"business_impact": 1,'
                        '"business_impact_modulation_name": "LowImpactOnDay",'
                        '"modulation_period": "day"},'
                        '{"business_impact": 1,'
                        '"business_impact_modulation_name": '
                        '"LowImpactOnNight",'
                        '"modulation_period": "night"}]'
                   )

            businessimpactmodulations = (self.client.config.
                                         businessimpactmodulations.list())

            self.assertEqual(
                businessimpactmodulations,
                [{"business_impact": 1,
                  "business_impact_modulation_name": "LowImpactOnDay",
                  "modulation_period": "day"},
                 {"business_impact": 1,
                  "business_impact_modulation_name": "LowImpactOnNight",
                  "modulation_period": "night"}, ]
            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/"
                  "businessimpactmodulations",
                  text='{"business_impact": 1,'
                       '"business_impact_modulation_name": "testtt",'
                       '"modulation_period": "day"}'
                  )

            self.client.config.businessimpactmodulations.create(
                business_impact=1,
                business_impact_modulation_name="testtt",
                modulation_period="day"
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "business_impact": 1,
                    "business_impact_modulation_name": "testtt",
                    "modulation_period": "day"
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get('http://localhost:5311/v2/config/businessimpactmodulations/'
                  'LowImpactOnDay',
                  text='{"business_impact": 1,'
                       '"business_impact_modulation_name": "LowImpactOnDay",'
                       '"modulation_period": "day"}'
                  )

            businessimpactmodulation = (
                self.client.config.businessimpactmodulations.get(
                    businessimpactmodulation_name='LowImpactOnDay')
                )

            self.assertEqual(
                businessimpactmodulation,
                {"business_impact": 1,
                 "business_impact_modulation_name": "LowImpactOnDay",
                 "modulation_period": "day"}
            )

    def test_update(self):
        with requests_mock.mock() as m:
            m.put('http://localhost:5311/v2/config/'
                  'businessimpactmodulations/LowImpactOnNight',
                  text='{"test": "test"}'
                  )

            self.client.config.businessimpactmodulations.update(
                businessimpactmodulation_name="LowImpactOnNight",
                businessimpactmodulation={'modulation_period': 'night'}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "modulation_period": u"night"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/"
                     "businessimpactmodulations/name_to_delete",
                     text="body"
                     )

            body = self.client.config.businessimpactmodulations.delete(
                businessimpactmodulation_name="name_to_delete",
            )

            self.assertEqual(
                body,
                "body"
            )
