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


class TestContacts(clienttest.ClientTest):
    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/contacts",
                   text='[{"contact_name": "bobby",'
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

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/contacts",
                  text='{"contact_name": "John"}')

            self.client.config.contacts.create(
                contact_name='John'
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "contact_name": "John"
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get('http://localhost:5311/v2/config/contacts/bobby',
                  text='{"contact_name": "bobby",'
                       '"email": "bob@bob.com"}')

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

    def test_update(self):
        with requests_mock.mock() as m:
            m.put('http://localhost:5311/v2/config/contacts/bob',
                  text='{"test": "test"}')

            self.client.config.contacts.update(
                contact_name="bob",
                contact={"email": "updated"}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "email": u"updated"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/contacts/bob",
                     text="body")

            body = self.client.config.contacts.delete(
                contact_name="bob",
            )

            self.assertEqual(
                body,
                "body"
            )
