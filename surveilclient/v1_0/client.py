# Copyright 2014 - Savoir-Faire Linux inc.
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

from surveilclient.common import http
from surveilclient.v1_0 import hosts
from surveilclient.v1_0 import services


class Client(object):

    """Client for the Surveil v1_0 API.

    :param string endpoint: The url of the surveil API
    """

    def __init__(self, endpoint):
        self.http_client = http.HTTPClient(endpoint, authenticated=False)
        self.hosts = hosts.HostsManager(self.http_client)
        self.services = services.ServicesManager(self.http_client)

    def reload_config(self):
        resp, body = self.http_client.json_request(
            '/reload_config',
            'POST',
            body=''  # Must send empty body
        )
        return body
