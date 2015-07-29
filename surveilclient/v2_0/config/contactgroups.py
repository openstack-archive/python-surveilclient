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


class ContactGroupsManager(surveil_manager.SurveilManager):
    base_url = '/config/contactgroups'

    def list(self, query=None):
        """Get a list of contactgroups."""
        query = query or {}
        resp, body = self.http_client.json_request(
            ContactGroupsManager.base_url, 'POST',
            body=query
        )
        return body

    def create(self, **kwargs):
        """Create a new contactgroup."""
        resp, body = self.http_client.json_request(
            ContactGroupsManager.base_url, 'PUT',
            body=kwargs
        )
        return body

    def get(self, contactgroup_name):
        """Get a new contactgroup."""
        resp, body = self.http_client.json_request(
            ContactGroupsManager.base_url + '/' + contactgroup_name, 'GET',
            body=''
        )
        return body

    def update(self, contactgroup_name, contactgroup):
        """Update a contactgroup."""
        resp, body = self.http_client.json_request(
            ContactGroupsManager.base_url + '/' + contactgroup_name, 'PUT',
            body=contactgroup
        )
        return body

    def delete(self, contactgroup_name):
        """Delete a contactgroup."""
        resp, body = self.http_client.request(
            ContactGroupsManager.base_url + "/" + contactgroup_name,
            'DELETE',
            body=''
        )
        return body