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
from surveilclient.v2_0.config import businessimpactmodulations
from surveilclient.v2_0.config import checkmodulations
from surveilclient.v2_0.config import commands
from surveilclient.v2_0.config import contactgroups
from surveilclient.v2_0.config import contacts
from surveilclient.v2_0.config import hostgroups
from surveilclient.v2_0.config import hosts
from surveilclient.v2_0.config import macromodulations
from surveilclient.v2_0.config import notificationways
from surveilclient.v2_0.config import realms
from surveilclient.v2_0.config import servicegroups
from surveilclient.v2_0.config import services
from surveilclient.v2_0.config import timeperiods


class ConfigManager(surveil_manager.SurveilManager):
    base_url = '/config'

    def __init__(self, http_client):
        super(ConfigManager, self).__init__(http_client)
        self.businessimpactmodulations = (businessimpactmodulations.
                                          BusinessImpactModulationsManager(
                                              self.http_client))
        self.checkmodulations = checkmodulations.CheckModulationsManager(
            self.http_client)
        self.commands = commands.CommandsManager(self.http_client)
        self.contacts = contacts.ContactsManager(self.http_client)
        self.contactgroups = contactgroups.ContactGroupsManager(
            self.http_client)
        self.hosts = hosts.HostsManager(self.http_client)
        self.hostgroups = hostgroups.HostGroupsManager(self.http_client)
        self.macromodulations = macromodulations.MacroModulationsManager(
            self.http_client)
        self.notificationways = notificationways.NotificationWaysManager(
            self.http_client)
        self.realms = realms.RealmsManager(self.http_client)
        self.services = services.ServicesManager(self.http_client)
        self.servicegroups = servicegroups.ServiceGroupsManager(
            self.http_client)
        self.timeperiods = timeperiods.TimePeriodsManager(self.http_client)

    def reload_config(self):
        resp, body = self.http_client.json_request(
            self.base_url + '/reload_config',
            'POST',
            body=''  # Must send empty body
        )
        return body
