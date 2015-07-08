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

        events = self.client.status.events.list(host_name='sfl.com',
                                                service_description='cpu',
                                                event_type='ALERT',
                                                page_size=50,
                                                page=5)

        filters = json.loads(
            httpretty.last_request().body.decode())['filters']
        self.assertEqual(
            json.loads(filters)['is'],
            {"service_description": ["cpu"],
             "host_name": ["sfl.com"], "event_type": ["ALERT"]}
        )

        paging = json.loads(
            httpretty.last_request().body.decode())['paging']
        self.assertEqual(
            paging,
            {u"page": 5,
             u"size": 50}
        )

        self.assertEqual(
            events,
            [{"host_name": "sfl.com", "service_description": "cpu",
              "event_type": "ALERT", "output": "Ok"},
             {"host_name": "sfl.com", "service_description": "cpu",
              "event_type": "ALERT", "output": "Not Ok"}]
        )

    @httpretty.activate
    def test_list_with_live_query(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:5311/v2/status/events",
            body='[{"host_name": "sfl.com", "service_description": "cpu", '
                 '"event_type": "ALERT", "output": "Ok"},'
                 '{"host_name": "sfl.com", "service_description": "cpu", '
                 '"event_type": "ALERT", "output": "Not Ok"}]'
        )

        events = self.client.status.events.list(
            live_query='{"filters": {"is": {"host_name": ["sfl.com"], '
                       '"event_type": ["ALERT"]},'
                       '"isnot": {"service_description": ["load"]}}}',
            start_time='2015-05-22T13:38:08Z',
            end_time='2015-05-22T13:42:08Z'
        )

        filters = json.loads(httpretty.last_request().body.decode())['filters']
        self.assertEqual(
            json.loads(filters)['is'],
            {"host_name": ["sfl.com"], "event_type": ["ALERT"]}
        )
        self.assertEqual(
            json.loads(filters)['isnot'],
            {"service_description": ["load"]}
        )

        self.assertEqual(
            json.loads(
                httpretty.last_request().body.decode())['time_interval'],
            {u"start_time": u"2015-05-22T13:38:08Z",
             u"end_time": u"2015-05-22T13:42:08Z"}
        )

        self.assertEqual(
            events,
            [{"host_name": u"sfl.com", "service_description": u"cpu",
              "event_type": u"ALERT", "output": u"Ok"},
             {"host_name": u"sfl.com", "service_description": u"cpu",
              "event_type": u"ALERT", "output": u"Not Ok"}]
        )
