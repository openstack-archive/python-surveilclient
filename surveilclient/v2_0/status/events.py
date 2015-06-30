# Copyright 2014-2015 - Savoir-Faire Linux inc.
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

from surveilclient.common import surveil_manager


class EventsManager(surveil_manager.SurveilManager):
    base_url = '/status/events'

    def list(self, host_name=None, service_description=None, event_type=None,
             start_time=None, end_time=None, live_query=None):
        """List events."""

        if live_query is None:
            live_query = {}
        else:
            live_query = json.loads(live_query)

        if start_time and end_time:
            live_query['time_interval'] = {
                "start_time": start_time,
                "end_time": end_time
            }

        if 'filters' not in live_query:
            live_query['filters'] = {}

        if 'is' not in live_query['filters']:
            live_query['filters']['is'] = {}

        if host_name:
            live_query['filters']['is']['host_name'] = [host_name]

        if service_description:
            (live_query['filters']['is']
                ['service_description']) = [service_description]

        if event_type:
            live_query['filters']['is']['event_type'] = [event_type]

        live_query['filters'] = json.dumps(live_query['filters'])

        resp, body = self.http_client.json_request(
            EventsManager.base_url, 'POST', body=live_query
        )
        return body
