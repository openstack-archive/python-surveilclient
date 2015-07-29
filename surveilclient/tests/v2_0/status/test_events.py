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

import httpretty

from surveilclient.tests.v2_0 import clienttest


class TestEvents(clienttest.ClientTest):

    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:5311/v2/status/events",
            body='[{"host_name": "sfl.com", "service_description": "cpu", '
                 '"event_type": "ALERT", "output": "Ok"},'
                 '{"host_name": "sfl.com", "service_description": "cpu", '
                 '"event_type": "ALERT", "output": "Not Ok"}]'
        )

        events = self.client.status.events.list()
        self.assertEqual(
            events,
            [{"host_name": "sfl.com", "service_description": "cpu",
              "event_type": "ALERT", "output": "Ok"},
             {"host_name": "sfl.com", "service_description": "cpu",
              "event_type": "ALERT", "output": "Not Ok"}]
        )