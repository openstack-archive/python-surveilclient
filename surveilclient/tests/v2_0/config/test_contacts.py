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


class TestContacts(clienttest.ClientTest):
    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.GET, "http://localhost:5311/v2/config/contacts",
            body='[{"contact_name": "bobby",'
                 '"email": "bob@bob.com"},'
                 '{"contact_name": "marie",'
                 '"email": "marie@marie.com"}]'
        )

        contacts = self.client.config.contacts.list()

        self.assertEqual(
            contacts,
            [
                {
                    'contact_name': 'bobby',
                    'email': 'bob@bob.com'
                },
                {
                    'contact_name': 'marie',
                    'email': 'marie@marie.com'
                },
            ]

        )

    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:5311/v2/config/contacts",
            body='{"contact_name": "John"}'
        )

        self.client.config.contacts.create(
            contact_name='John'
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "contact_name": "John"
            }
        )

    @httpretty.activate
    def test_show(self):
        httpretty.register_uri(
            httpretty.GET,
            'http://localhost:5311/v2/config/contacts/bobby',
            body='{"contact_name": "bobby",'
                 '"email": "bob@bob.com"}'
        )

        contact = self.client.config.contacts.get(
            contact_name='bobby'
        )

        self.assertEqual(
            contact,
            {
                'contact_name': 'bobby',
                'email': 'bob@bob.com'
            }
        )

    @httpretty.activate
    def test_update(self):
        httpretty.register_uri(
            httpretty.PUT,
            'http://localhost:5311/v2/config/contacts/bob',
            body='{"test": "test"}'
        )

        self.client.config.contacts.update(
            contact_name="bob",
            contact={"email": "updated"}
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "email": u"updated"
            }
        )

    @httpretty.activate
    def test_delete(self):
        httpretty.register_uri(
            httpretty.DELETE,
            "http://localhost:5311/v2/config/contacts/bob",
            body="body"
        )

        body = self.client.config.contacts.delete(
            contact_name="bob",
        )

        self.assertEqual(
            body,
            "body"
        )
