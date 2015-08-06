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


class CheckModulationsManager(surveil_manager.SurveilManager):
    base_url = '/config/checkmodulations'

    def list(self, query=None):
        """Get a list of checkmodulations."""
        query = query or {}
        resp, body = self.http_client.json_request(
            CheckModulationsManager.base_url, 'POST', data=query
        )
        return body

    def create(self, **kwargs):
        """Create a new checkmodulation."""
        resp, body = self.http_client.json_request(
            CheckModulationsManager.base_url, 'PUT',
            data=kwargs
        )
        return body

    def get(self, checkmodulation_name):
        """Get a new checkmodulation."""
        resp, body = self.http_client.json_request(
            CheckModulationsManager.base_url + '/' +
            checkmodulation_name, 'GET',
            data=''
        )
        return body

    def update(self, checkmodulation_name, checkmodulation):
        """Update a checkmodulation."""
        resp, body = self.http_client.json_request(
            CheckModulationsManager.base_url + '/' +
            checkmodulation_name, 'PUT',
            data=checkmodulation
        )
        return body

    def delete(self, checkmodulation_name):
        """Delete a checkmodulation."""
        resp, body = self.http_client.request(
            CheckModulationsManager.base_url+"/" + checkmodulation_name,
            'DELETE'
        )
        return body
