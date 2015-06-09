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


class CommandsManager(surveil_manager.SurveilManager):
    base_url = '/config/commands'

    def list(self):
        """Get a list of commands."""
        resp, body = self.http_client.json_request(
            CommandsManager.base_url, 'GET'
        )
        return body

    def create(self, **kwargs):
        """Create a new command."""
        resp, body = self.http_client.json_request(
            CommandsManager.base_url, 'POST',
            body=kwargs
        )
        return body

    def get(self, command_name):
        """Get a new command."""
        resp, body = self.http_client.json_request(
            CommandsManager.base_url + '/' + command_name, 'GET',
            body=''
        )
        return body

    def update(self, **kwargs):
        """Update a command."""
        resp, body = self.http_client.json_request(
            CommandsManager.base_url + '/' + kwargs['command_name'], 'PUT',
            body=kwargs
        )
        return body

    def delete(self, command_name):
        """Delete a command."""
        resp, body = self.http_client.request(
            CommandsManager.base_url + "/" + command_name,
            'DELETE',
            body=''
        )
        return body