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


class MacroModulationsManager(surveil_manager.SurveilManager):
    base_url = '/config/macromodulations'

    def list(self, query={}):
        """Get a list of macromodulations."""
        resp, body = self.http_client.json_request(
            MacroModulationsManager.base_url, 'POST',
            body=query
        )
        return body

    def create(self, **kwargs):
        """Create a new macromodulation."""
        resp, body = self.http_client.json_request(
            MacroModulationsManager.base_url, 'PUT',
            body=kwargs
        )
        return body

    def get(self, macromodulation_name):
        """Get a new macromodulation."""
        resp, body = self.http_client.json_request(
            MacroModulationsManager.base_url + '/' +
            macromodulation_name, 'GET',
            body=''
        )
        return body

    def update(self, macromodulation_name, macromodulation):
        """Update a macromodulation."""
        resp, body = self.http_client.json_request(
            MacroModulationsManager.base_url + '/' +
            macromodulation_name, 'PUT',
            body=macromodulation
        )
        return body

    def delete(self, macromodulation_name):
        """Delete a macromodulation."""
        resp, body = self.http_client.request(
            MacroModulationsManager.base_url + "/" + macromodulation_name,
            'DELETE',
            body=''
        )
        return body