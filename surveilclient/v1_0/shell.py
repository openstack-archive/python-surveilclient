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

from surveilclient.common import utils


def do_host_list(sc, args):
    """List all hosts."""
    hosts = sc.hosts.list()

    if args.json:
        print(utils.json_formatter(hosts))
    else:
        cols = [
            'host_name',
            'address',
        ]

        formatters = {
            'host_name': lambda x: x['host_name'],
            'address': lambda x: x['address'],
        }
        utils.print_list(hosts, cols, formatters=formatters)


def do_service_list(sc, args):
    """List all services."""
    services = sc.services.list()

    if args.json:
        print(utils.json_formatter(services))
    else:
        cols = [
            'host_name',
            'service_description',
            'check_period',
            'contact_groups',
        ]

        formatters = {
            'service_description': lambda x: x['service_description'],
            'host_name': lambda x: x['host_name'],
            'check_period': lambda x: x['check_period'],
            'contact_groups': lambda x: x['contact_groups'],
        }
        utils.print_list(services, cols, formatters=formatters)


def do_reload_config(sc, args):
    """Trigger a config reload."""
    print (sc.reload_config()['message'])
