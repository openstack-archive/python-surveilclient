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


class TestMacroModulations(clienttest.ClientTest):
    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/macromodulations",
                   text='[{"macromodulation_name": "HighDuringNight",'
                        '"modulation_period": "night",'
                        '"_CRITICAL": 20,'
                        '"_WARNING": 10},'
                        '{"macromodulation_name": "LowDuringNight",'
                        '"modulation_period": "night",'
                        '"_CRITICAL": 10,'
                        '"_WARNING": 20}]')

            contacts = self.client.config.macromodulations.list()

            self.assertEqual(
                contacts,
                [
                    {
                        'macromodulation_name': 'HighDuringNight',
                        'modulation_period': 'night',
                        '_CRITICAL': 20,
                        '_WARNING': 10,
                    },
                    {
                        'macromodulation_name': 'LowDuringNight',
                        'modulation_period': 'night',
                        '_CRITICAL': 10,
                        '_WARNING': 20,
                    }
                ]
            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/macromodulations",
                  text='{"macromodulation_name": "TEST_CREATE_MODULATION",'
                       '"modulation_period": "night"}')

            self.client.config.macromodulations.create(
                macromodulation_name='TEST_CREATE_MODULATION',
                modulation_period='night'
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "macromodulation_name": "TEST_CREATE_MODULATION",
                    "modulation_period": "night"
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get('http://localhost:5311/v2/config/'
                  'macromodulations/HighDuringNight',
                  text='{"macromodulation_name": "HighDuringNight",'
                       '"modulation_period": "night"}')

            macromodulation = self.client.config.macromodulations.get(
                macromodulation_name='HighDuringNight'
            )

            self.assertEqual(
                macromodulation,
                {
                    'macromodulation_name': 'HighDuringNight',
                    'modulation_period': 'night'
                }
            )

    def test_update(self):
        with requests_mock.mock() as m:
            m.put('http://localhost:5311/v2/config/'
                  'macromodulations/HighDuringNight',
                  text='{"test": "test"}')

            self.client.config.macromodulations.update(
                macromodulation_name="HighDuringNight",
                macromodulation={"modulation_period": "updated"}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "modulation_period": u"updated"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/macromodulations/test",
                     text="body")

            body = self.client.config.macromodulations.delete(
                macromodulation_name="test",
            )

            self.assertEqual(
                body,
                "body"
            )
