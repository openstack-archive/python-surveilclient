# Copyright 2015 - Savoir-Faire Linux inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json

import requests_mock

from surveilclient.tests.v2_0 import clienttest


class TestTimePeriods(clienttest.ClientTest):
    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/timeperiods",
                   text='['
                        '{'
                        '"timeperiod_name": "nonworkhours",'
                        '"sunday": "00:00-24:00",'
                        '"monday": "00:00-09:00,17:00-24:00"'
                        '},'
                        '{'
                        '"timeperiod_name": "misc-single-days",'
                        '"1999-01-28": "00:00-24:00",'
                        '"day 2": "00:00-24:00"'
                        '}'
                        ']')

            timeperiods = self.client.config.timeperiods.list()

            self.assertEqual(
                timeperiods,
                [
                    {
                        'timeperiod_name': 'nonworkhours',
                        'sunday': '00:00-24:00',
                        'monday': '00:00-09:00,17:00-24:00'
                    },
                    {
                        'timeperiod_name': 'misc-single-days',
                        '1999-01-28': '00:00-24:00',
                        'day 2': '00:00-24:00',
                    },
                ]

            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/timeperiods",
                  text='{"timeperiod_name": "John"}')

            self.client.config.timeperiods.create(
                timeperiod_name='new_periods'
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "timeperiod_name": "new_periods"
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get('http://localhost:5311/v2/config/timeperiods/nonworkhours',
                  text='{'
                       '"timeperiod_name": "nonworkhours",'
                       '"sunday": "00:00-24:00",'
                       '"monday": "00:00-09:00,17:00-24:00"'
                       '}')

            timeperiod = self.client.config.timeperiods.get(
                timeperiod_name='nonworkhours'
            )

            self.assertEqual(
                timeperiod,
                {
                    'timeperiod_name': 'nonworkhours',
                    'sunday': '00:00-24:00',
                    'monday': '00:00-09:00,17:00-24:00'
                }
            )

    def test_update(self):
        with requests_mock.mock() as m:
            m.put('http://localhost:5311/v2/config/timeperiods/nonworkhours',
                  text='{"test": "test"}')

            self.client.config.timeperiods.update(
                timeperiod_name="nonworkhours",
                timeperiod={"timeperiod_name": "updated"}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "timeperiod_name": u"updated"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/timeperiods/bob",
                     text="body")

            body = self.client.config.timeperiods.delete(
                timeperiod_name="bob",
            )

            self.assertEqual(
                body,
                "body"
            )
