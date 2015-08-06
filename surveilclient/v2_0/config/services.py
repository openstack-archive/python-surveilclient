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


class ServicesManager(surveil_manager.SurveilManager):
    base_url = '/config/services'

    def list(self, query=None, templates=False):
        """Get a list of hosts."""
        query = query or {}
        if not templates:
            if 'filters' not in query:
                query["filters"] = '{}'
            filters = json.loads(query["filters"])
            temp_filter = {"register": ["0"]}
            if 'isnot' not in filters:
                filters["isnot"] = temp_filter
            else:
                filters["isnot"].update(temp_filter)
            query['filters'] = json.dumps(filters)

        resp, body = self.http_client.json_request(
            ServicesManager.base_url, 'POST',
            body=query
        )
        return body

    def create(self, **kwargs):
        """Create a new host."""
        resp, body = self.http_client.json_request(
            ServicesManager.base_url, 'PUT',
            body=kwargs
        )
        return body

    def delete(self, host_name, service_description):
        """Delete a service."""
        resp, body = self.http_client.request(
            '/config/hosts' + '/'
            + host_name + '/services/' + service_description,
            'DELETE',
            body=''
        )
        return body

    def get(self, host_name, service_description):
        """Get a service."""
        resp, body = self.http_client.json_request(
            '/config/hosts/' + host_name +
            '/services/' + service_description,
            'GET',
            body=''
        )
        return body
