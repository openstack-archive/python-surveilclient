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


class TestServiceGroups(clienttest.ClientTest):
    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:5311/v2/config/servicegroups",
            body='[{"servicegroup_name": "dbservices",'
                 '"members": "ms1,SQL Server,ms1,'
                 'SQL Serverc Agent,ms1,SQL DTC"},'
                 '{"servicegroup_name": "otherservices",'
                 '"members": "some,other,member"}]'
        )

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

    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.PUT, "http://localhost:5311/v2/config/servicegroups",
            body='{"servicegroup_name": "John",'
                 '"members": "marie,bob,joe"}'
        )

        self.client.config.servicegroups.create(
            servicegroup_name='John',
            members="marie,bob,joe"
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "servicegroup_name": "John",
                "members": "marie,bob,joe"
            }
        )

    @httpretty.activate
    def test_get(self):
        httpretty.register_uri(
            httpretty.GET,
            'http://localhost:5311/v2/config/servicegroups/dbservices',
            body='{"servicegroup_name": "dbservices",'
                 '"members": "ms1,SQL Server,ms1,'
                 'SQL Serverc Agent,ms1,SQL DTC"}'
        )

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

    @httpretty.activate
    def test_update(self):
        httpretty.register_uri(
            httpretty.PUT,
            'http://localhost:5311/v2/config/servicegroups/dbservices',
            body='{"test": "test"}'
        )

        self.client.config.servicegroups.update(
            servicegroup_name="dbservices",
            servicegroup={"members": "updated"}
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
            "http://localhost:5311/v2/config/servicegroups/dbservices",
            body="body"
        )

        body = self.client.config.servicegroups.delete(
            servicegroup_name="dbservices",
        )

        self.assertEqual(
            body,
            "body"
        )
