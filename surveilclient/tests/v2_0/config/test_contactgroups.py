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


class TestContactGroups(clienttest.ClientTest):
    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/contactgroups",
                   text='[{"contactgroup_name": "novell-admins",'
                        '"members": "jdoe,rtobert,tzach"},'
                        '{"contactgroup_name": "linux-adminx",'
                        '"members": "linus,richard"}]'
                   )

            contactgroups = self.client.config.contactgroups.list()

            self.assertEqual(
                contactgroups,
                [{"contactgroup_name": "novell-admins",
                  "members": "jdoe,rtobert,tzach"},
                 {"contactgroup_name": "linux-adminx",
                  "members": "linus,richard"},
                 ]
            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/contactgroups",
                  text='{"contactgroup_name": "John",'
                       '"members": "marie,bob,joe"}'
                  )

            self.client.config.contactgroups.create(
                contactgroup_name='John',
                members="marie,bob,joe"
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "contactgroup_name": "John",
                    "members": "marie,bob,joe"
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get('http://localhost:5311/v2/'
                  'config/contactgroups/novell-admins',
                  text='{"contactgroup_name": "novell-admins",'
                       '"members": "jdoe,rtobert,tzach"}'
                  )

            contactgroup = self.client.config.contactgroups.get(
                contactgroup_name='novell-admins'
            )

            self.assertEqual(
                contactgroup,
                {
                    'contactgroup_name': 'novell-admins',
                    'members': 'jdoe,rtobert,tzach'
                }
            )

    def test_update(self):
        with requests_mock.mock() as m:
            m.put('http://localhost:5311/v2/config/contactgroups/'
                  'novell-admins',
                  text='{"test": "test"}'
                  )

            self.client.config.contactgroups.update(
                contactgroup_name="novell-admins",
                contactgroup={"members": "updated"}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "members": u"updated"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/contactgroups/"
                     "novell-admins",
                     text="body"
                     )

            body = self.client.config.contactgroups.delete(
                contactgroup_name="novell-admins",
            )

            self.assertEqual(
                body,
                "body"
            )
