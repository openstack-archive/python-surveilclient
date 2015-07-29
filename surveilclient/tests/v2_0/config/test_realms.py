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


class TestRealms(clienttest.ClientTest):
    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:5311/v2/config/realms",
            body='['
                 '{'
                 '"realm_name": "World",'
                 '"realm_members": "Europe,America,Asia",'
                 '"default": 0'
                 '},'
                 '{'
                 '"realm_name": "Anti-world",'
                 '"realm_members": "void,black-hole",'
                 '"default": 1'
                 '}'
                 ']'
        )

        realms = self.client.config.realms.list()

        self.assertEqual(
            realms,
            [
                {
                    'realm_name': 'World',
                    'realm_members': 'Europe,America,Asia',
                    'default': 0
                },
                {
                    'realm_name': 'Anti-world',
                    'realm_members': 'void,black-hole',
                    'default': 1
                },
            ]

        )

    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.PUT, "http://localhost:5311/v2/config/realms",
            body='{"realm_name": "John",'
                 '"realm_members":"marie,bob,joe",'
                 '"default":1}'
        )

        self.client.config.realms.create(
            realm_name='John',
            realm_members="marie,bob,joe",
            default=1
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "realm_name": "John",
                "realm_members": "marie,bob,joe",
                "default": 1
            }
        )

    @httpretty.activate
    def test_get(self):
        httpretty.register_uri(
            httpretty.GET,
            'http://localhost:5311/v2/config/realms/bobby',
            body='{'
                 '"realm_name": "World",'
                 '"realm_members": "Europe,America,Asia",'
                 '"default": 0'
                 '}'
        )

        realm = self.client.config.realms.get(
            realm_name='bobby'
        )

        self.assertEqual(
            realm,
            {
                'realm_name': 'World',
                'realm_members': 'Europe,America,Asia',
                'default': 0
            }
        )

    @httpretty.activate
    def test_update(self):
        httpretty.register_uri(
            httpretty.PUT,
            'http://localhost:5311/v2/config/realms/World',
            body='{"test": "test"}'
        )

        self.client.config.realms.update(
            realm_name="World",
            realm={"realm_members": "updated"}
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "realm_members": u"updated"
            }
        )

    @httpretty.activate
    def test_delete(self):
        httpretty.register_uri(
            httpretty.DELETE,
            "http://localhost:5311/v2/config/realms/bob",
            body="body"
        )

        body = self.client.config.realms.delete(
            realm_name="bob",
        )

        self.assertEqual(
            body,
            "body"
        )
