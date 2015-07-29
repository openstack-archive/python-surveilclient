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


class HostGroupsManager(surveil_manager.SurveilManager):
    base_url = '/config/hostgroups'

    def list(self, query=None):
        """Get a list of hostgroups."""
        query = query or {}
        resp, body = self.http_client.json_request(
            HostGroupsManager.base_url, 'POST',
            body=query
        )
        return body

    def create(self, **kwargs):
        """Create a new hostgroup."""
        resp, body = self.http_client.json_request(
            HostGroupsManager.base_url, 'PUT',
            body=kwargs
        )
        return body

    def get(self, hostgroup_name):
        """Get a new hostgroup."""
        resp, body = self.http_client.json_request(
            HostGroupsManager.base_url + '/' + hostgroup_name, 'GET',
            body=''
        )
        return body

    def update(self, hostgroup_name, hostgroup):
        """Update a hostgroup."""
        resp, body = self.http_client.json_request(
            HostGroupsManager.base_url + '/' + hostgroup_name, 'PUT',
            body=hostgroup
        )
        return body

    def delete(self, hostgroup_name):
        """Delete a hostgroup."""
        resp, body = self.http_client.request(
            HostGroupsManager.base_url + "/" + hostgroup_name,
            'DELETE',
            body=''
        )
        return body