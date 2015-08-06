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


class TestHostGroups(clienttest.ClientTest):
    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/hostgroups",
                   text='[{"hostgroup_name": "novell-servers",'
                        '"members": "netware1,netware2,netware3,netware4"},'
                        '{"hostgroup_name": "otherservers",'
                        '"members": "googul,sfl"}]'
                   )

            hostgroups = self.client.config.hostgroups.list()

            self.assertEqual(
                hostgroups,
                [
                    {
                        'hostgroup_name': 'novell-servers',
                        'members': 'netware1,netware2,netware3,netware4',
                    },
                    {
                        'hostgroup_name': 'otherservers',
                        'members': 'googul,sfl',
                    },
                ]
            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/hostgroups",
                  text='{"hostgroup_name": "John",'
                       '"members": "marie,bob,joe"}')

            self.client.config.hostgroups.create(
                hostgroup_name='John',
                members="marie,bob,joe"
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "hostgroup_name": "John",
                    "members": "marie,bob,joe"
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get('http://localhost:5311/v2/config/hostgroups/novell-servers',
                  text='{"hostgroup_name": "novell-servers",'
                       '"members": "netware1,netware2,netware3,netware4"}')

            hostgroup = self.client.config.hostgroups.get(
                hostgroup_name='novell-servers'
            )

            self.assertEqual(
                hostgroup,
                {
                    'hostgroup_name': 'novell-servers',
                    'members': 'netware1,netware2,netware3,netware4'
                }
            )

    def test_update(self):
        with requests_mock.mock() as m:
            m.put('http://localhost:5311/v2/config/hostgroups/novell-servers')

            self.client.config.hostgroups.update(
                hostgroup_name="novell-servers",
                hostgroup={"members": "updated"}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "members": u"updated"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/hostgroups/novell-servers",
                     text="body")

            body = self.client.config.hostgroups.delete(
                hostgroup_name="novell-servers",
            )

            self.assertEqual(
                body,
                "body"
            )
