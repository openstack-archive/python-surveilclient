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
            'host_name': lambda x: x['host_name'],
            'address': lambda x: x['address'],
        }
        utils.print_list(hosts, cols, formatters=formatters)


@cliutils.arg("host_name", help="Name of the host")
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


@cliutils.arg("host_name", help="Name of the host")
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
            'check_command': lambda x: x['check_command'],
            'check_period': lambda x: x['check_period'],
            'checkmodulation_name': lambda x: x['checkmodulation_name']
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


@cliutils.arg("host_name", help="Name of the host")
@cliutils.arg("metric_name", help="Name of the metric")
@cliutils.arg("time_begin", help="begin of the metric")
@cliutils.arg("time_end", help="end of the metric")
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


@cliutils.arg("host_name", help="Name of the host")
@cliutils.arg("metric_name", help="Name of the metric")
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


@cliutils.arg("host_name", help="Name of the host")
@cliutils.arg("--service_description", help="Service description")
@cliutils.arg("--time_stamp")
def do_action_recheck(sc, args):
    """Schedule a recheck."""
    arg_names = ['host_name',
                 'service_description',
                 'time_stamp']

    recheck = _dict_from_args(args, arg_names)
    sc.actions.recheck.create(**recheck)
