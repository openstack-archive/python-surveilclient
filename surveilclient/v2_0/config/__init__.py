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
from surveilclient.v2_0.config import checkmodulations
from surveilclient.v2_0.config import commands
from surveilclient.v2_0.config import hosts
from surveilclient.v2_0.config import services


class ConfigManager(surveil_manager.SurveilManager):
    base_url = '/config'

    def __init__(self, http_client):
        super(ConfigManager, self).__init__(http_client)
        self.checkmodulations = checkmodulations.CheckModulationsManager(
            self.http_client)
        self.commands = commands.CommandsManager(self.http_client)
        self.hosts = hosts.HostsManager(self.http_client)
        self.services = services.ServicesManager(self.http_client)

    def reload_config(self):
        resp, body = self.http_client.json_request(
            self.base_url + '/reload_config',
            'POST',
            body=''  # Must send empty body
        )
        return body
