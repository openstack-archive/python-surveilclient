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


class TestHostGroups(clienttest.ClientTest):
    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:5311/v2/config/hostgroups",
            body='[{"hostgroup_name": "novell-servers",'
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

    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.PUT, "http://localhost:5311/v2/config/hostgroups",
            body='{"hostgroup_name": "John",'
                 '"members": "marie,bob,joe"}'
        )

        self.client.config.hostgroups.create(
            hostgroup_name='John',
            members="marie,bob,joe"
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "hostgroup_name": "John",
                "members": "marie,bob,joe"
            }
        )

    @httpretty.activate
    def test_get(self):
        httpretty.register_uri(
            httpretty.GET,
            'http://localhost:5311/v2/config/hostgroups/novell-servers',
            body='{"hostgroup_name": "novell-servers",'
                 '"members": "netware1,netware2,netware3,netware4"}'
        )

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

    @httpretty.activate
    def test_update(self):
        httpretty.register_uri(
            httpretty.PUT,
            'http://localhost:5311/v2/config/hostgroups/novell-servers',
            body='{"test": "test"}'
        )

        self.client.config.hostgroups.update(
            hostgroup_name="novell-servers",
            hostgroup={"members": "updated"}
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "members": u"updated"
            }
        )

    @httpretty.activate
    def test_delete(self):
        httpretty.register_uri(
            httpretty.DELETE,
            "http://localhost:5311/v2/config/hostgroups/novell-servers",
            body="body"
        )

        body = self.client.config.hostgroups.delete(
            hostgroup_name="novell-servers",
        )

        self.assertEqual(
            body,
            "body"
        )
