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


class TestMetrics(clienttest.ClientTest):

    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:8080/v2/status/"
                            "hosts/localhost/metrics/load1",
            body='[{"min": "2", "warning": "15", "value": "3"},'
                 '{"min": "5", "warning": "200", "value": "150"}]'
        )

        metrics = self.client.status.hosts.metrics.get('localhost', 'load1',
                                                       time_begin='2015-05-22'
                                                                  'T13:38:08Z',
                                                       time_end='2015-05-'
                                                                '22T13:38:08Z')

        self.assertEqual(
            metrics,
            [{"min": "2", "warning": "15", "value": "3"},
             {"min": "5", "warning": "200", "value": "150"}]
        )

    @httpretty.activate
    def test_list_service(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:8080/v2/status/hosts/localhost"
                            "/services/load/metrics/load1",
            body='[{"min": "2", "warning": "15", "value": "3"},'
                 '{"min": "5", "warning": "200", "value": "150"}]'
        )

        metrics = self.client.status.hosts.metrics.get('localhost', 'load1',
                                                       'load',
                                                       '2015-05-22T13:38:08Z',
                                                       '2015-05-22T13:38:08Z'
                                                       )

        self.assertEqual(
            metrics,
            [{"min": "2", "warning": "15", "value": "3"},
             {"min": "5", "warning": "200", "value": "150"}]
        )

    @httpretty.activate
    def test_show(self):
        httpretty.register_uri(
            httpretty.GET, "http://localhost:8080/v2/status/hosts/localhost"
                           "/metrics/load1",
            body='{"min": "2", "warning": "15", "value": "3"}'
        )

        metrics = self.client.status.hosts.metrics.get('localhost', 'load1')

        self.assertEqual(
            metrics,
            {"min": "2", "warning": "15", "value": "3"}
        )

    @httpretty.activate
    def test_show_service(self):
        httpretty.register_uri(
            httpretty.GET, "http://localhost:8080/v2/status/hosts/localhost"
                           "/services/load/metrics/load1",
            body='{"min": "2", "warning": "15", "value": "3"}'
        )

        metrics = self.client.status.hosts.metrics.get('localhost', 'load1',
                                                       'load')

        self.assertEqual(
            metrics,
            {"min": "2", "warning": "15", "value": "3"}
        )
