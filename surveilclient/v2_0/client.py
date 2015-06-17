# Copyright 2015 - Savoir-Faire Linux inc.
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

import os

from surveilclient.common import http
from surveilclient.v2_0 import actions
from surveilclient.v2_0 import config
from surveilclient.v2_0 import status


class Client(object):

    """Client for the Surveil v2_0 API.

    :param string endpoint: The url of the surveil API
    """

    def __init__(self,
                 endpoint,
                 username=os.environ.get('OS_USERNAME', None),
                 password=os.environ.get('OS_PASSWORD', None),
                 tenant_name=os.environ.get('OS_TENANT_NAME', None),
                 auth_url=None):

        if auth_url is None:
            auth_url = os.environ.get(
                'SURVEIL_AUTH_URL',
                os.environ.get('OS_AUTH_URL', endpoint + '/auth')
            )
            if auth_url is None:
                raise Exception("Must specify auth url")

        self.http_client = http.HTTPClient(
            endpoint,
            username=username,
            password=password,
            tenant_name=tenant_name,
            auth_url=auth_url,
        )

        self.config = config.ConfigManager(self.http_client)
        self.status = status.StatusManager(self.http_client)
        self.actions = actions.ActionsManager(self.http_client)
