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


class TimePeriodsManager(surveil_manager.SurveilManager):
    base_url = '/config/timeperiods'

    def list(self, query=None):
        """Get a list of timeperiods."""
        query = query or {}
        resp, body = self.http_client.json_request(
            TimePeriodsManager.base_url, 'POST',
            data=query
        )
        return body

    def create(self, **kwargs):
        """Create a new timeperiod."""
        resp, body = self.http_client.json_request(
            TimePeriodsManager.base_url, 'PUT',
            data=kwargs
        )
        return body

    def get(self, timeperiod_name):
        """Get a new timeperiod."""
        resp, body = self.http_client.json_request(
            TimePeriodsManager.base_url + '/' + timeperiod_name, 'GET'
        )
        return body

    def update(self, timeperiod_name, timeperiod):
        """Update a timeperiod."""
        resp, body = self.http_client.json_request(
            TimePeriodsManager.base_url + '/' + timeperiod_name, 'PUT',
            data=timeperiod
        )
        return body

    def delete(self, timeperiod_name):
        """Delete a timeperiod."""
        resp, body = self.http_client.request(
            TimePeriodsManager.base_url + "/" + timeperiod_name,
            'DELETE'
        )
        return body
