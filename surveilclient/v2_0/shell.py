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

import json

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
            'host_name': lambda x: x.get('host_name', ''),
            'address': lambda x: x.get('address', '')
        }
        utils.print_list(hosts, cols, formatters=formatters)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--address", help="Address of the host")
@cliutils.arg("--max_check_attempts")
@cliutils.arg("--check_period")
@cliutils.arg("--contacts")
@cliutils.arg("--contact_groups")
@cliutils.arg("--custom_fields")
@cliutils.arg("--notification_interval")
@cliutils.arg("--notification_period")
@cliutils.arg("--use")
def do_config_host_update(sc, args):
    """Create a config host."""
    arg_names = ['address',
                 'max_check_attempts',
                 'check_period',
                 'contacts',
                 'contact_groups',
                 'custom_fields',
                 'notification_interval',
                 'notification_period',
                 'use']
    host = _dict_from_args(args, arg_names)

    host["host_name"] = args.host_name

    if "custom_fields" in host:
        host["custom_fields"] = json.loads(host["custom_fields"])

    sc.config.hosts.update(args.host_name, **host)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--address", help="Address of the host")
@cliutils.arg("--max_check_attempts")
@cliutils.arg("--check_period")
@cliutils.arg("--contacts")
@cliutils.arg("--contact_groups")
@cliutils.arg("--custom_fields")
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
                 'custom_fields',
                 'notification_interval',
                 'notification_period',
                 'use']
    host = _dict_from_args(args, arg_names)

    if "custom_fields" in host:
        host["custom_fields"] = json.loads(host["custom_fields"])

    sc.config.hosts.create(**host)


@cliutils.arg("--host_name", help="Name of the host")
def do_config_host_show(sc, args):
    """Show a specific host."""
    host = sc.config.hosts.get(args.host_name)

    if args.json:
        print(utils.json_formatter(host))
    elif host:
        """ Specify the shown order and all the properties to display """
        hostProperties = [
            'host_name', 'address', 'check_period', 'contact_groups',
            'contacts', 'custom_fields', 'max_check_attempts',
            'notification_interval', 'notification_period', 'use'
        ]

        utils.print_item(host, hostProperties)


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
            'service_description': lambda x: x.get('service_description', ''),
            'host_name': lambda x: x.get('host_name', ''),
            'check_period': lambda x: x.get('check_period', ''),
            'contact_groups': lambda x: x.get('contact_groups', ''),
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
@cliutils.arg("--passive_checks_enabled")
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
                 'passive_checks_enabled',
                 'use']
    service = _dict_from_args(args, arg_names)
    sc.config.services.create(**service)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--service_description", help="The service_description")
def do_config_service_delete(sc, args):
    """Create a config host."""
    sc.config.services.delete(args.host_name,
                              args.service_description)


def do_config_checkmodulation_list(sc, args):
    """List all config check modulations."""
    checkmodulations = sc.config.checkmodulations.list()

    if args.json:
        print(utils.json_formatter(checkmodulations))
    else:
        cols = [
            'check_command',
            'check_period',
            'checkmodulation_name'
        ]

        formatters = {
            'check_command': lambda x: x.get('check_command', ''),
            'check_period': lambda x: x.get('check_period', ''),
            'checkmodulation_name': lambda x: x.get('checkmodulation_name',
                                                    ''),
        }
        utils.print_list(checkmodulations, cols, formatters=formatters)


@cliutils.arg("--check_command")
@cliutils.arg("--check_period")
@cliutils.arg("--checkmodulation_name")
def do_config_checkmodulation_create(sc, args):
    """Create a config check modulation."""
    arg_names = ['check_command',
                 'check_period',
                 'checkmodulation_name']
    checkmodulation = _dict_from_args(args, arg_names)
    sc.config.checkmodulations.create(**checkmodulation)


@cliutils.arg("--checkmodulation_name", help="Name of the check modulation")
def do_config_checkmodulation_delete(sc, args):
    """Create a config check modulation."""
    sc.config.checkmodulations.delete(args.checkmodulation_name)


def do_config_command_list(sc, args):
    """List all config commands."""
    commands = sc.config.commands.list()

    if args.json:
        print(utils.json_formatter(commands))
    else:
        cols = [
            'command_name',
            'command_line'
        ]

        formatters = {
            'command_name': lambda x: x.get('command_name', ''),
            'command_line': lambda x: x.get('command_line', ''),
        }
        utils.print_list(commands, cols, formatters=formatters)


@cliutils.arg("--command_name")
@cliutils.arg("--command_line")
def do_config_command_create(sc, args):
    """Create a config check modulation."""
    arg_names = ['command_name',
                 'command_line']
    command = _dict_from_args(args, arg_names)
    sc.config.commands.create(**command)


@cliutils.arg("--command_name", help="Name of the command")
def do_config_command_delete(sc, args):
    """Delete a config command."""
    sc.config.commands.delete(args.command_name)


@cliutils.arg("--command_name", help="Name of the command")
def do_config_command_show(sc, args):
    """Show a specific command."""
    command = sc.config.commands.get(args.command_name)

    if args.json:
        print(utils.json_formatter(command))
    elif command:
        """ Specify the shown order and all the properties to display """
        command_properties = [
            'command_name', 'command_line'
        ]

        utils.print_item(command, command_properties)


@cliutils.arg("--command_name", help="Name of the command")
@cliutils.arg("--command_line", help="Address of the command")
def do_config_command_update(sc, args):
    """Update a config command."""
    arg_names = ['command_name',
                 'command_line']
    command = _dict_from_args(args, arg_names)
    sc.config.commands.update(**command)


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
            'host_name': lambda x: x.get('host_name', ''),
            'address': lambda x: x.get('address', ''),
            'state': lambda x: x.get('state', ''),
            'last_check': lambda x: x.get('last_check', ''),
            'plugin_output': lambda x: x.get('plugin_output',
                                             '')[0:30] + '...',
        }
        utils.print_list(services, cols, formatters=formatters)


@cliutils.arg("--host_name", help="The host_name")
def do_status_host_show(sc, args):
    host = sc.status.hosts.get(args.host_name)

    if args.json:
        print(utils.json_formatter(host))
    elif host:
        hostProperties = [
            'host_name', 'address', 'state', 'last_check',
            'last_state_change', 'long_output', 'description', 'acknowledged',
            'plugin_output', 'services', 'childs', 'parents',
        ]
        utils.print_item(host, hostProperties)


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
            'host_name': lambda x: x.get('host_name', ''),
            'service_description': lambda x: x.get('service_description', ''),
            'state': lambda x: x.get('state', ''),
            'last_check': lambda x: x.get('last_check', ''),
            'plugin_output': lambda x: x.get('plugin_output', '')[0:30],
        }
        utils.print_list(services, cols, formatters=formatters)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--metric_name", help="Name of the metric")
@cliutils.arg("--time_begin", help="begin of the metric")
@cliutils.arg("--time_end", help="end of the metric")
@cliutils.arg("--service_description", help="Service description")
def do_status_metrics_list(sc, args):
    """List all status metrics."""
    arg_names = ['host_name',
                 'metric_name',
                 'time_begin',
                 'time_end',
                 'service_description']
    arg = _dict_from_args(args, arg_names)

    metrics = sc.status.hosts.metrics.get(**arg)
    if args.json:
        print(utils.json_formatter(metrics))
    else:
        cols = [
            'min',
            'max',
            'warning',
            'critical',
            'value',
            'unit'
        ]

        formatters = {
            'min': lambda x: x.get('min', ''),
            'max': lambda x: x.get('max', ''),
            'warning': lambda x: x.get('warning', ''),
            'critical': lambda x: x.get('critical', ''),
            'value': lambda x: x.get('value', ''),
            'unit': lambda x: x.get('unit', ''),
        }
        utils.print_list(metrics, cols, formatters=formatters)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--metric_name", help="Name of the metric")
@cliutils.arg("--service_description", help="Service description")
def do_status_metrics_show(sc, args):
    """Give the last status metrics."""
    arg_names = ['host_name',
                 'metric_name',
                 'service_description']
    arg = _dict_from_args(args, arg_names)

    metric = sc.status.hosts.metrics.get(**arg)
    if args.json:
        print(utils.json_formatter(metric))
    else:
        metricProperties = [
            'min',
            'max',
            'warning',
            'critical',
            'value',
            'unit'
        ]

        utils.print_item(metric, metricProperties)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--service_description", help="Service description")
@cliutils.arg("--output", help="The output of the plugin")
@cliutils.arg("--return_code", help="The return code of the plugin")
def do_status_submit_check_result(sc, args):
    """Submit a check result."""
    if args.service_description:
        sc.status.services.submit_check_result(
            args.host_name,
            args.service_description,
            output=args.output,
            return_code=int(args.return_code),
        )
    else:
        sc.status.hosts.submit_check_result(
            args.host_name,
            output=args.output,
            return_code=int(args.return_code),
        )


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--service_description", help="Service description")
@cliutils.arg("--time_stamp")
def do_action_recheck(sc, args):
    """Schedule a recheck."""
    arg_names = ['host_name',
                 'service_description',
                 'time_stamp']

    recheck = _dict_from_args(args, arg_names)
    sc.actions.recheck.create(**recheck)
