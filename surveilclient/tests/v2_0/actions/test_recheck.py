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


class TestRecheck(clienttest.ClientTest):

    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:5311/v2/actions/recheck",
            body='{"message": "Ack received!"}')

        self.client.actions.recheck.create(
            host_name="somehost",
            service_description="someservice"
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {"host_name": "somehost", "service_description": "someservice"}
        )
