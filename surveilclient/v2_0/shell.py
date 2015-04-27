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

from surveilclient.common import utils
from surveilclient.openstack.common import cliutils


def _dict_from_args(args, arg_names):
    result = {}
    for arg in arg_names:
        value = getattr(args, arg, None)
        if value is not None:
            result[arg] = value

    return result


def do_config_host_list(sc, args):
    """List all config hosts."""
    hosts = sc.config.hosts.list()

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


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--address", help="Address of the host")
@cliutils.arg("--max_check_attempts")
@cliutils.arg("--check_period")
@cliutils.arg("--contacts")
@cliutils.arg("--contact_groups")
@cliutils.arg("--notification_interval")
@cliutils.arg("--notification_period")
@cliutils.arg("--use")
def do_config_host_create(sc, args):
    """Create a config host."""
    arg_names = ['host_name',
                 'address',
                 'max_check_attempts',
                 'check_period',
                 'contacts',
                 'contact_groups',
                 'notification_interval',
                 'notification_period',
                 'use']
    host = _dict_from_args(args, arg_names)
    sc.config.hosts.create(**host)


@cliutils.arg("--host_name", help="Name of the host")
def do_config_host_delete(sc, args):
    """Create a config host."""
    sc.config.hosts.delete(args.host_name)


def do_config_service_list(sc, args):
    """List all config services."""
    services = sc.config.services.list()

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


@cliutils.arg("--host_name")
@cliutils.arg("--service_description")
@cliutils.arg("--check_command")
@cliutils.arg("--max_check_attempts")
@cliutils.arg("--check_interval")
@cliutils.arg("--retry_interval")
@cliutils.arg("--check_period")
@cliutils.arg("--notification_interval")
@cliutils.arg("--notification_period")
@cliutils.arg("--contacts")
@cliutils.arg("--contact_groups")
def do_config_service_create(sc, args):
    """Create a config service."""
    arg_names = ['host_name',
                 'service_description',
                 'check_command',
                 'max_check_attempts',
                 'check_interval',
                 'retry_interval',
                 'check_period',
                 'notification_interval',
                 'notification_period',
                 'contacts',
                 'contact_groups',
                 'use']
    service = _dict_from_args(args, arg_names)
    sc.config.services.create(**service)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--service_description")
def do_config_service_delete(sc, args):
    """Create a config host."""
    sc.config.services.delete(args.host_name,
                              args.service_description)


def do_config_reload(sc, args):
    """Trigger a config reload."""
    print(sc.config.reload_config()['message'])


def do_status_host_list(sc, args):
    """List all status hosts."""
    services = sc.status.hosts.list()

    if args.json:
        print(utils.json_formatter(services))
    else:
        cols = [
            'host_name',
            'address',
            'state',
            'last_check',
            'plugin_output',
        ]

        formatters = {
            'host_name': lambda x: x['host_name'],
            'address': lambda x: x['address'],
            'state': lambda x: x['state'],
            'last_check': lambda x: x['last_check'],
            'plugin_output': lambda x: x['plugin_output'][0:30] + '...',
        }
        utils.print_list(services, cols, formatters=formatters)


def do_status_service_list(sc, args):
    """List all status services."""
    services = sc.status.services.list()

    if args.json:
        print(utils.json_formatter(services))
    else:
        cols = [
            'host_name',
            'service_description',
            'state',
            'last_check',
            'plugin_output',
        ]

        formatters = {
            'host_name': lambda x: x['host_name'],
            'service_description': lambda x: x['service_description'],
            'state': lambda x: x['state'],
            'last_check': lambda x: x['last_check'],
            'plugin_output': lambda x: x['plugin_output'][0:30] + '...',
        }
        utils.print_list(services, cols, formatters=formatters)
