# Copyright 2014-2015 - Savoir-Faire Linux inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from surveilclient.common import surveil_manager


class MetricsManager(surveil_manager.SurveilManager):
    base_url = '/status/hosts'

    def get(self, host_name, metric_name, service_description=None,
            time_begin=None, time_end=None):
        if time_begin is not None and time_end is not None:
            """Get a list of metrics."""
            time_delta = {'begin': time_begin,
                          'end': time_end}
            if service_description is not None:
                url = (MetricsManager.base_url + "/" + host_name + "/services/"
                       + service_description + "/metrics/" + metric_name)
            else:
                url = (MetricsManager.base_url + "/" + host_name + "/metrics/"
                       + metric_name)

            resp, body = self.http_client.json_request(
                url, 'POST', body=time_delta
            )
            return body
        elif time_begin is None and time_end is None:

            if service_description is not None:
                url = (MetricsManager.base_url + "/" + host_name + "/services/"
                       + service_description + "/metrics/" + metric_name)
            else:
                url = (MetricsManager.base_url + "/" + host_name + "/metrics/"
                       + metric_name)

            resp, body = self.http_client.json_request(url, 'GET')
            return body
        else:
            return {}