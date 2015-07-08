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

from surveilclient.common import surveil_manager
from surveilclient.common import utils


class EventsManager(surveil_manager.SurveilManager):
    base_url = '/status/events'

    def list(self, host_name=None, service_description=None, event_type=None,
             start_time=None, end_time=None, live_query=None, size=None, page=None):
        """List events."""

        filters = {
            'is': {
                'host_name': host_name,
                'service_description': service_description,
                'event_type': event_type
            }
        }

        query = utils.create_query(
            query=live_query,
            filters=filters,
            start_time=start_time,
            end_time=end_time,
            size=size,
            page=page
        )

        resp, body = self.http_client.json_request(
            EventsManager.base_url, 'POST', body=query
        )
        return body
