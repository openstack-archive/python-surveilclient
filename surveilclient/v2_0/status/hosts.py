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
from surveilclient.v2_0.status.metrics import metrics


class HostsManager(surveil_manager.SurveilManager):
    base_url = '/status/hosts'

    def __init__(self, http_client):
        super(HostsManager, self).__init__(http_client)
        self.metrics = metrics.MetricsManager(self.http_client)

    def list(self, live_query={'filters': '{}'}):
        """Get a list of hosts."""
        resp, body = self.http_client.json_request(
            HostsManager.base_url, 'POST', body=live_query
        )
        return body

    def get(self, host_name):
        """Get a specific host."""
        resp, body = self.http_client.json_request(
            HostsManager.base_url + "/" + host_name, 'GET'
        )
        return body

    def submit_check_result(self, host_name, **kwargs):
        """Submit a check result."""
        resp, body = self.http_client.json_request(
            HostsManager.base_url + '/' + host_name + '/results', 'POST',
            body=kwargs
        )
        return body
