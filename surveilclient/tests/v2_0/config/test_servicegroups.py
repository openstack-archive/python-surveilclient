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


class TestServiceGroups(clienttest.ClientTest):
    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/servicegroups",
                   text='[{"servicegroup_name": "dbservices",'
                        '"members": "ms1,SQL Server,ms1,'
                        'SQL Serverc Agent,ms1,SQL DTC"},'
                        '{"servicegroup_name": "otherservices",'
                        '"members": "some,other,member"}]')

            servicegroups = self.client.config.servicegroups.list()

            self.assertEqual(
                servicegroups,
                [
                    {
                        'servicegroup_name': 'dbservices',
                        'members': 'ms1,SQL Server,ms1,'
                                   'SQL Serverc Agent,ms1,SQL DTC',
                    },
                    {
                        'servicegroup_name': 'otherservices',
                        'members': 'some,other,member',
                    },
                ]
            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/servicegroups",
                  text='{"servicegroup_name": "John",'
                       '"members": "marie,bob,joe"}')

            self.client.config.servicegroups.create(
                servicegroup_name='John',
                members="marie,bob,joe"
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "servicegroup_name": "John",
                    "members": "marie,bob,joe"
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get('http://localhost:5311/v2/config/servicegroups/dbservices',
                  text='{"servicegroup_name": "dbservices",'
                       '"members": "ms1,SQL Server,ms1,'
                       'SQL Serverc Agent,ms1,SQL DTC"}')

            servicegroup = self.client.config.servicegroups.get(
                servicegroup_name='dbservices'
            )

            self.assertEqual(
                servicegroup,
                {
                    'servicegroup_name': 'dbservices',
                    'members': 'ms1,SQL Server,ms1,SQL Serverc Agent,ms1,SQL DTC'
                }
            )

    def test_update(self):
        with requests_mock.mock() as m:
            m.put('http://localhost:5311/v2/config/servicegroups/dbservices',
                  text='{"test": "test"}')

            self.client.config.servicegroups.update(
                servicegroup_name="dbservices",
                servicegroup={"members": "updated"}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "members": u"updated"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/servicegroups/dbservices",
                     text="body")

            body = self.client.config.servicegroups.delete(
                servicegroup_name="dbservices",
            )

            self.assertEqual(
                body,
                "body"
            )
