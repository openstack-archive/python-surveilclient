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


class TestMacroModulations(clienttest.ClientTest):
    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:5311/v2/config/macromodulations",
            body='[{"macromodulation_name": "HighDuringNight",'
                 '"modulation_period": "night",'
                 '"_CRITICAL": 20,'
                 '"_WARNING": 10},'
                 '{"macromodulation_name": "LowDuringNight",'
                 '"modulation_period": "night",'
                 '"_CRITICAL": 10,'
                 '"_WARNING": 20}]'
        )

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

    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.PUT, "http://localhost:5311/v2/config/macromodulations",
            body='{"macromodulation_name": "TEST_CREATE_MODULATION",'
                 '"modulation_period": "night"}'
        )

        self.client.config.macromodulations.create(
            macromodulation_name='TEST_CREATE_MODULATION',
            modulation_period='night'
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "macromodulation_name": "TEST_CREATE_MODULATION",
                "modulation_period": "night"
            }
        )

    @httpretty.activate
    def test_get(self):
        httpretty.register_uri(
            httpretty.GET,
            'http://localhost:5311/v2/config/macromodulations/HighDuringNight',
            body='{"macromodulation_name": "HighDuringNight",'
                 '"modulation_period": "night"}'
        )

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

    @httpretty.activate
    def test_update(self):
        httpretty.register_uri(
            httpretty.PUT,
            'http://localhost:5311/v2/config/macromodulations/HighDuringNight',
            body='{"test": "test"}'
        )

        self.client.config.macromodulations.update(
            macromodulation_name="HighDuringNight",
            macromodulation={"modulation_period": "updated"}
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "modulation_period": u"updated"
            }
        )

    @httpretty.activate
    def test_delete(self):
        httpretty.register_uri(
            httpretty.DELETE,
            "http://localhost:5311/v2/config/macromodulations/test",
            body="body"
        )

        body = self.client.config.macromodulations.delete(
            macromodulation_name="test",
        )

        self.assertEqual(
            body,
            "body"
        )
