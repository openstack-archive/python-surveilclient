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


class HostsManager(surveil_manager.SurveilManager):
    base_url = '/config/hosts'

    def list(self, query=None, templates=False):
        """Get a list of hosts."""
        query = query or {}
        if templates:
            if 'filters' not in query:
                query["filters"] = '{}'
            filters = json.loads(query["filters"])
            temp_filter = {"register": ["0"]}
            if 'is' not in filters:
                filters["is"] = temp_filter
            else:
                filters["is"].update(temp_filter)
            query['filters'] = json.dumps(query['filters'])

        resp, body = self.http_client.json_request(
            HostsManager.base_url, 'POST',
            body=query
        )
        return body

    def create(self, **kwargs):
        """Create a new host."""
        resp, body = self.http_client.json_request(
            HostsManager.base_url, 'PUT',
            body=kwargs
        )
        return body

    def get(self, host_name):
        """Get a new host."""
        resp, body = self.http_client.json_request(
            HostsManager.base_url + '/' + host_name, 'GET',
            body=''
        )
        return body

    def update(self, host_name, host):
        """Update a host."""
        resp, body = self.http_client.json_request(
            HostsManager.base_url + '/' + host_name, 'PUT',
            body=host
        )
        return body

    def delete(self, host_name):
        """Delete a host."""
        resp, body = self.http_client.request(
            HostsManager.base_url + '/' + host_name, 'DELETE',
            body=''
        )
        return body
