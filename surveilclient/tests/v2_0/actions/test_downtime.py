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

import requests_mock

from surveilclient.tests.v2_0 import clienttest


class TestDowntime(clienttest.ClientTest):

    def test_create(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/actions/downtime",
                   text='{"message": "Ack received!"}')

            self.client.actions.downtime.create(
                host_name="somehost"
            )
            self.assertEqual(
                m.last_request.body,
                u'{"host_name": "somehost"}'
            )
