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


@cliutils.arg("--business_impact_modulation_name",
              help="New name of the business impact modulation")
@cliutils.arg("--business_impact")
@cliutils.arg("--modulation_period")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_businessimpactmodulation_list(sc, args):
    """List all config business impact modulations."""
    arg_names = ['business_impact_modulation_name',
                 'business_impact',
                 'modulation_period',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    businessimpactmodulations = sc.config.businessimpactmodulations.list(lq)

    if args.json:
        print(utils.json_formatter(businessimpactmodulations))
    else:
        cols = [
            'business_impact_modulation_name',
            'business_impact',
            'modulation_period'
        ]

        formatters = {
            'business_impact_modulation_name': lambda x: x.get(
                'business_impact_modulation_name', ''),
            'business_impact': lambda x: x.get('business_impact', ''),
            'modulation_period': lambda x: x.get('modulation_period', '')
        }
        utils.print_list(businessimpactmodulations, cols,
                         formatters=formatters)


@cliutils.arg("--original_business_impact_modulation_name",
              help="Original name of the business impact modulation")
@cliutils.arg("--business_impact_modulation_name",
              help="New name of the business impact modulation")
@cliutils.arg("--business_impact")
@cliutils.arg("--modulation_period")
def do_config_businessimpactmodulation_update(sc, args):
    """Update a config business impact modulation."""
    arg_names = ['business_impact_modulation_name',
                 'business_impact',
                 'modulation_period'
                 ]
    businessimpactmodulation = _dict_from_args(args, arg_names)
    sc.config.businessimpactmodulations.update(
        args.original_business_impact_modulation_name,
        businessimpactmodulation)


@cliutils.arg("--business_impact_modulation_name",
              help="Name of the business impact modulation")
@cliutils.arg("--business_impact")
@cliutils.arg("--modulation_period")
def do_config_businessimpactmodulation_create(sc, args):
    """Create a config business impact modulation."""
    arg_names = ['business_impact_modulation_name',
                 'business_impact',
                 'modulation_period'
                 ]
    businessimpactmodulation = _dict_from_args(args, arg_names)
    sc.config.businessimpactmodulations.create(**businessimpactmodulation)


@cliutils.arg("--business_impact_modulation_name",
              help="Name of the business impact modulation")
def do_config_businessimpactmodulation_show(sc, args):
    """Show a specific business impact modulation."""
    businessimpactmodulation = sc.config.businessimpactmodulations.get(
        args.business_impact_modulation_name)

    if args.json:
        print(utils.json_formatter(businessimpactmodulation))
    elif businessimpactmodulation:
        """ Specify the shown order and all the properties to display """
        businessimpactmodulationProperties = [
            'business_impact_modulation_name',
            'business_impact',
            'modulation_period']

        utils.print_item(businessimpactmodulation,
                         businessimpactmodulationProperties)


@cliutils.arg("--business_impact_modulation_name",
              help="Name of the business impact modulation")
def do_config_businessimpactmodulation_delete(sc, args):
    """Delete a config business impact modulation."""
    sc.config.businessimpactmodulations.delete(
        args.business_impact_modulation_name)


@cliutils.arg("--checkmodulation_name",
              help="New name of the check modulation")
@cliutils.arg("--check_command")
@cliutils.arg("--check_period")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_checkmodulation_list(sc, args):
    """List all config check modulations."""
    arg_names = ['checkmodulation_name',
                 'check_command',
                 'check_period',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)

    lq = utils.create_query(**arg_dict)
    checkmodulations = sc.config.checkmodulations.list(lq)

    if args.json:
        print(utils.json_formatter(checkmodulations))
    else:
        cols = [
            'checkmodulation_name',
            'check_command',
            'check_period'
        ]

        formatters = {
            'checkmodulation_name': lambda x: x.get('checkmodulation_name',
                                                    ''),
            'check_command': lambda x: x.get('check_command', ''),
            'check_period': lambda x: x.get('check_period', '')
        }
        utils.print_list(checkmodulations, cols, formatters=formatters)


@cliutils.arg("original_checkmodulation_name",
              help="Original name of the check modulation")
@cliutils.arg("--checkmodulation_name",
              help="New name of the check modulation")
@cliutils.arg("--check_command")
@cliutils.arg("--check_period")
def do_config_checkmodulation_update(sc, args):
    """Update a config check modulation."""
    arg_names = ['checkmodulation_name',
                 'check_command',
                 'check_period'
                 ]
    checkmodulation = _dict_from_args(args, arg_names)
    sc.config.checkmodulations.update(
        args.original_checkmodulation_name, checkmodulation)


@cliutils.arg("--checkmodulation_name")
@cliutils.arg("--check_command")
@cliutils.arg("--check_period")
def do_config_checkmodulation_create(sc, args):
    """Create a config check modulation."""
    arg_names = ['checkmodulation_name',
                 'check_command',
                 'check_period'
                 ]
    checkmodulation = _dict_from_args(args, arg_names)
    sc.config.checkmodulations.create(**checkmodulation)


@cliutils.arg("--checkmodulation_name", help="Name of the check modulation")
def do_config_checkmodulation_show(sc, args):
    """Show a specific check modulation."""
    checkmodulation = sc.config.checkmodulations.get(args.checkmodulation_name)

    if args.json:
        print(utils.json_formatter(checkmodulation))
    elif checkmodulation:
        """ Specify the shown order and all the properties to display """
        checkmodulationProperties = [
            'checkmodulation_name',
            'check_command',
            'check_period']

        utils.print_item(checkmodulation, checkmodulationProperties)


@cliutils.arg("--checkmodulation_name", help="Name of the check modulation")
def do_config_checkmodulation_delete(sc, args):
    """Delete a config check modulation."""
    sc.config.checkmodulations.delete(args.checkmodulation_name)


@cliutils.arg("--command_name", help="New name of the command")
@cliutils.arg("--command_line", help="Address of the command")
@cliutils.arg("--module_type")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_command_list(sc, args):
    """List all config commands."""
    arg_names = ['command_name',
                 'command_line',
                 'module_type',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    commands = sc.config.commands.list(lq)

    if args.json:
        print(utils.json_formatter(commands))
    else:
        cols = [
            'command_name',
            'command_line',
            'module_type'
        ]

        formatters = {
            'command_name': lambda x: x.get('command_name', ''),
            'command_line': lambda x: x.get('command_line', ''),
            'module_type': lambda x: x.get('module_type', ''),
        }
        utils.print_list(commands, cols, formatters=formatters)


@cliutils.arg("original_command_name", help="Original name of the command")
@cliutils.arg("--command_name", help="New name of the command")
@cliutils.arg("--command_line", help="Address of the command")
@cliutils.arg("--module_type")
def do_config_command_update(sc, args):
    """Update a config command."""
    arg_names = ['command_name',
                 'command_line',
                 'module_type']
    command = _dict_from_args(args, arg_names)
    sc.config.commands.update(args.original_command_name, command)


@cliutils.arg("--command_name")
@cliutils.arg("--command_line")
@cliutils.arg("--module_type")
def do_config_command_create(sc, args):
    """Create a config command."""
    arg_names = ['command_name',
                 'command_line',
                 'module_type']
    command = _dict_from_args(args, arg_names)
    sc.config.commands.create(**command)


@cliutils.arg("--command_name", help="Name of the command")
def do_config_command_show(sc, args):
    """Show a specific command."""
    command = sc.config.commands.get(args.command_name)

    if args.json:
        print(utils.json_formatter(command))
    elif command:
        """ Specify the shown order and all the properties to display """
        command_properties = [
            'command_name', 'command_line', 'module_type'
        ]

        utils.print_item(command, command_properties)


@cliutils.arg("--command_name", help="Name of the command")
def do_config_command_delete(sc, args):
    """Delete a config command."""
    sc.config.commands.delete(args.command_name)


@cliutils.arg("--contactgroup_name", help="New name of the contactgroup")
@cliutils.arg("--members")
@cliutils.arg("--alias")
@cliutils.arg("--contactgroup_members")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_contactgroup_list(sc, args):
    """List all contact groups."""
    arg_names = ['contactgroup_name',
                 'members',
                 'alias',
                 'contactgroup_members',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    contactgroups = sc.config.contactgroups.list(lq)

    if args.json:
        print(utils.json_formatter(contactgroups))
    else:
        cols = [
            'contactgroup_name',
            'members',
            'alias',
            'contactgroup_members'
        ]

        formatters = {
            'contactgroup_name': lambda x: x.get('contactgroup_name', ''),
            'members': lambda x: x.get('members', ''),
            'alias': lambda x: x.get('alias', ''),
            'contactgroup_members': lambda x: x.get('contactgroup_members', '')
        }
        utils.print_list(contactgroups, cols, formatters=formatters)


@cliutils.arg("original_contactgroup_name",
              help="Original name of the contact group")
@cliutils.arg("--contactgroup_name", help="New name of the contactgroup")
@cliutils.arg("--members", nargs='+')
@cliutils.arg("--alias")
@cliutils.arg("--contactgroup_members", nargs='+')
def do_config_contactgroup_update(sc, args):
    """Update a config contact group."""
    arg_names = ['contactgroup_name',
                 'members',
                 'alias',
                 'contactgroup_members'
                 ]
    contactgroup = _dict_from_args(args, arg_names)
    sc.config.contactgroups.update(
        args.original_contactgroup_name, contactgroup)


@cliutils.arg("--contactgroup_name", help="New name of the contactgroup")
@cliutils.arg("--members", nargs='+')
@cliutils.arg("--alias")
@cliutils.arg("--contactgroup_members", nargs='+')
def do_config_contactgroup_create(sc, args):
    """Create a config contact group."""
    arg_names = ['contactgroup_name',
                 'members',
                 'alias',
                 'contactgroup_members'
                 ]
    contactgroup = _dict_from_args(args, arg_names)
    sc.config.contactgroups.create(**contactgroup)


@cliutils.arg("--contactgroup_name", help="Name of the contact group")
def do_config_contactgroup_show(sc, args):
    """Show a specific contact group."""
    contactgroup = sc.config.contactgroups.get(args.contactgroup_name)

    if args.json:
        print(utils.json_formatter(contactgroup))
    elif contactgroup:
        """ Specify the shown order and all the properties to display """
        contactgroupProperties = [
            'contactgroup_name',
            'members',
            'alias',
            'contactgroup_members'
        ]

        utils.print_item(contactgroup, contactgroupProperties)


@cliutils.arg("--contactgroup_name", help="Name of the contact group")
def do_config_contactgroup_delete(sc, args):
    """Delete a config contact group."""
    sc.config.contactgroups.delete(args.contactgroup_name)


@cliutils.arg("--contact_name", help="New name of the contact")
@cliutils.arg("--host_notifications_enabled")
@cliutils.arg("--service_notifications_enabled")
@cliutils.arg("--host_notification_period")
@cliutils.arg("--service_notification_period")
@cliutils.arg("--host_notification_options")
@cliutils.arg("--service_notification_options")
@cliutils.arg("--host_notification_commands")
@cliutils.arg("--service_notification_commands")
@cliutils.arg("--email")
@cliutils.arg("--pager")
@cliutils.arg("--can_submit_commands")
@cliutils.arg("--is_admin")
@cliutils.arg("--retain_status_information")
@cliutils.arg("--retain_nonstatus_information")
@cliutils.arg("--min_business_impact")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_contact_list(sc, args):
    """List all contacts."""
    arg_names = ['contact_name',
                 'host_notifications_enabled',
                 'service_notifications_enabled',
                 'host_notification_period',
                 'service_notification_period',
                 'host_notification_options',
                 'service_notification_options',
                 'host_notification_commands',
                 'service_notification_commands',
                 'email',
                 'pager',
                 'can_submit_commands',
                 'is_admin',
                 'retain_status_information',
                 'retain_nonstatus_information',
                 'min_business_impact',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    contacts = sc.config.contacts.list(lq)
    if args.json:
        print(utils.json_formatter(contacts))
    else:
        cols = [
            'contact_name',
            'host_notifications_enabled',
            'service_notifications_enabled',
            'host_notification_period',
            'service_notification_period',
            'host_notification_options',
            'service_notification_options',
            'host_notification_commands',
            'service_notification_commands',
            'email',
            'pager',
            'can_submit_commands',
            'is_admin',
            'retain_status_information',
            'retain_nonstatus_information',
            'min_business_impact'
        ]

        formatters = {
            'contact_name': lambda x: x.get('contact_name', ''),
            'host_notifications_enabled': lambda x: x.get(
                'host_notifications_enabled', ''),
            'service_notifications_enabled': lambda x: x.get(
                'service_notifications_enabled', ''),
            'host_notification_period': lambda x: x.get(
                'host_notification_period', ''),
            'service_notification_period': lambda x: x.get(
                'service_notification_period', ''),
            'host_notification_options': lambda x: x.get(
                'host_notification_options', ''),
            'service_notification_options': lambda x: x.get(
                'service_notification_options', ''),
            'host_notification_commands': lambda x: x.get(
                'host_notification_commands', ''),
            'service_notification_commands': lambda x: x.get(
                'service_notification_commands', ''),
            'email': lambda x: x.get('email', ''),
            'pager': lambda x: x.get('pager', ''),
            'can_submit_commands': lambda x: x.get('can_submit_commands', ''),
            'is_admin': lambda x: x.get('is_admin', ''),
            'retain_status_information': lambda x: x.get(
                'retain_status_information', ''),
            'retain_nonstatus_information': lambda x: x.get(
                'retain_nonstatus_information', ''),
            'min_business_impact': lambda x: x.get('min_business_impact', '')
        }
        utils.print_list(contacts, cols, formatters=formatters)


@cliutils.arg("original_contact_name", help="Original name of the contact ")
@cliutils.arg("--contact_name", help="New name of the contact")
@cliutils.arg("--host_notifications_enabled")
@cliutils.arg("--service_notifications_enabled")
@cliutils.arg("--host_notification_period")
@cliutils.arg("--service_notification_period")
@cliutils.arg("--host_notification_options", nargs='+')
@cliutils.arg("--service_notification_options", nargs='+')
@cliutils.arg("--host_notification_commands", nargs='+')
@cliutils.arg("--service_notification_commands", nargs='+')
@cliutils.arg("--email")
@cliutils.arg("--pager")
@cliutils.arg("--can_submit_commands")
@cliutils.arg("--is_admin")
@cliutils.arg("--retain_status_information", nargs='+')
@cliutils.arg("--retain_nonstatus_information", nargs='+')
@cliutils.arg("--min_business_impact")
def do_config_contact_update(sc, args):
    """Update a config contact."""
    arg_names = [
        'contact_name',
        'host_notifications_enabled',
        'service_notifications_enabled',
        'host_notification_period',
        'service_notification_period',
        'host_notification_options',
        'service_notification_options',
        'host_notification_commands',
        'service_notification_commands',
        'email',
        'pager',
        'can_submit_commands',
        'is_admin',
        'retain_status_information',
        'retain_nonstatus_information',
        'min_business_impact'
    ]
    contact = _dict_from_args(args, arg_names)
    sc.config.contacts.update(
        args.original_contact_name, contact)


@cliutils.arg("--contact_name", help="New name of the contact")
@cliutils.arg("--host_notifications_enabled")
@cliutils.arg("--service_notifications_enabled")
@cliutils.arg("--host_notification_period")
@cliutils.arg("--service_notification_period")
@cliutils.arg("--host_notification_options", nargs='+')
@cliutils.arg("--service_notification_options", nargs='+')
@cliutils.arg("--host_notification_commands", nargs='+')
@cliutils.arg("--service_notification_commands", nargs='+')
@cliutils.arg("--email")
@cliutils.arg("--pager")
@cliutils.arg("--can_submit_commands")
@cliutils.arg("--is_admin")
@cliutils.arg("--retain_status_information", nargs='+')
@cliutils.arg("--retain_nonstatus_information", nargs='+')
@cliutils.arg("--min_business_impact")
def do_config_contact_create(sc, args):
    """Create a config contact."""
    arg_names = [
        'contact_name',
        'host_notifications_enabled',
        'service_notifications_enabled',
        'host_notification_period',
        'service_notification_period',
        'host_notification_options',
        'service_notification_options',
        'host_notification_commands',
        'service_notification_commands',
        'email',
        'pager',
        'can_submit_commands',
        'is_admin',
        'retain_status_information',
        'retain_nonstatus_information',
        'min_business_impact'
    ]
    contact = _dict_from_args(args, arg_names)
    sc.config.contacts.create(**contact)


@cliutils.arg("--contact_name", help="Name of the contact")
def do_config_contact_show(sc, args):
    """Show a specific contact."""
    contact = sc.config.contacts.get(args.contact_name)

    if args.json:
        print(utils.json_formatter(contact))
    elif contact:
        """ Specify the shown order and all the properties to display """
        contactProperties = [
            'contact_name',
            'host_notifications_enabled',
            'service_notifications_enabled',
            'host_notification_period',
            'service_notification_period',
            'host_notification_options',
            'service_notification_options',
            'host_notification_commands',
            'service_notification_commands',
            'email',
            'pager',
            'can_submit_commands',
            'is_admin',
            'retain_status_information',
            'retain_nonstatus_information',
            'min_business_impact'
        ]

        utils.print_item(contact, contactProperties)


@cliutils.arg("--contact_name", help="Name of the contact")
def do_config_contact_delete(sc, args):
    """Delete a config contact."""
    sc.config.contacts.delete(args.contact_name)


@cliutils.arg("--hostgroup_name", help="New name of the host group")
@cliutils.arg("--members")
@cliutils.arg("--alias")
@cliutils.arg("--hostgroup_members")
@cliutils.arg("--notes")
@cliutils.arg("--notes_url")
@cliutils.arg("--action_url")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_hostgroup_list(sc, args):
    """List all config host groups."""
    arg_names = ['hostgroup_name',
                 'members',
                 'alias',
                 'hostgroup_members',
                 'notes',
                 'notes_url',
                 'action_url',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    hostgroups = sc.config.hostgroups.list(lq)

    if args.json:
        print(utils.json_formatter(hostgroups))
    else:
        cols = [
            'hostgroup_name',
            'members',
            'alias',
            'hostgroup_members',
            'notes',
            'notes_url',
            'action_url'
        ]

        formatters = {
            'hostgroup_name': lambda x: x.get('hostgroup_name', ''),
            'members': lambda x: x.get('members', ''),
            'alias': lambda x: x.get('alias', ''),
            'hostgroup_members': lambda x: x.get('hostgroup_members', ''),
            'notes': lambda x: x.get('notes', ''),
            'notes_url': lambda x: x.get('notes_url', ''),
            'action_url': lambda x: x.get('action_url', ''),

        }
        utils.print_list(hostgroups, cols, formatters=formatters)


@cliutils.arg("original_hostgroup_name",
              help="Original name of the host group")
@cliutils.arg("--hostgroup_name", help="New name of the host group")
@cliutils.arg("--members")
@cliutils.arg("--alias")
@cliutils.arg("--hostgroup_members")
@cliutils.arg("--notes")
@cliutils.arg("--notes_url")
@cliutils.arg("--action_url")
def do_config_hostgroup_update(sc, args):
    """Create a config host group."""
    arg_names = ['hostgroup_name',
                 'members',
                 'alias',
                 'hostgroup_members',
                 'notes',
                 'notes_url',
                 'action_url']
    hostgroup = _dict_from_args(args, arg_names)
    sc.config.hostgroups.update(args.original_hostgroup_name, hostgroup)


@cliutils.arg("--hostgroup_name", help="Name of the host group")
@cliutils.arg("--members", nargs='+')
@cliutils.arg("--alias")
@cliutils.arg("--hostgroup_members", nargs='+')
@cliutils.arg("--notes")
@cliutils.arg("--notes_url")
@cliutils.arg("--action_url")
def do_config_hostgroup_create(sc, args):
    """Create a config host group."""
    arg_names = ['hostgroup_name',
                 'members',
                 'alias',
                 'hostgroup_members',
                 'notes',
                 'notes_url',
                 'action_url']
    hostgroup = _dict_from_args(args, arg_names)

    sc.config.hostgroups.create(**hostgroup)


@cliutils.arg("--hostgroup_name", help="Name of the host")
def do_config_hostgroup_show(sc, args):
    """Show a specific host group."""
    hostgroup = sc.config.hostgroups.get(args.hostgroup_name)

    if args.json:
        print(utils.json_formatter(hostgroup))
    elif hostgroup:
        """ Specify the shown order and all the properties to display """
        hostgroupProperties = [
            'hostgroup_name',
            'members',
            'alias',
            'hostgroup_members',
            'notes',
            'notes_url',
            'action_url'
        ]

        utils.print_item(hostgroup, hostgroupProperties)


@cliutils.arg("--hostgroup_name", help="Name of the host group")
def do_config_hostgroup_delete(sc, args):
    """Delete a config host group."""
    sc.config.hostgroups.delete(args.hostgroup_name)


@cliutils.arg("--host_name", help="New name of the host")
@cliutils.arg("--address", help="Address of the host")
@cliutils.arg("--max_check_attempts")
@cliutils.arg("--check_period")
@cliutils.arg("--contacts", nargs='+')
@cliutils.arg("--contact_groups", nargs='+')
@cliutils.arg("--custom_fields")
@cliutils.arg("--notification_interval")
@cliutils.arg("--notification_period")
@cliutils.arg("--use", nargs='+')
@cliutils.arg("--name")
@cliutils.arg("--register")
@cliutils.arg("--check_interval")
@cliutils.arg("--retry_interval")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_host_list(sc, args):
    """List all config hosts."""
    arg_names = ['host_name',
                 'address',
                 'live_query',
                 'page_size',
                 'page',
                 'max_check_attempts',
                 'check_period',
                 'contacts',
                 'contact_groups',
                 'custom_fields',
                 'notification_interval',
                 'notification_period',
                 'use',
                 'name',
                 'register',
                 'check_interval',
                 'retry_interval'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    hosts = sc.config.hosts.list(lq)

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


@cliutils.arg("original_host_name", help="Original name of the host")
@cliutils.arg("--host_name", help="New name of the host")
@cliutils.arg("--address", help="Address of the host")
@cliutils.arg("--max_check_attempts")
@cliutils.arg("--check_period")
@cliutils.arg("--contacts", nargs='+')
@cliutils.arg("--contact_groups", nargs='+')
@cliutils.arg("--custom_fields")
@cliutils.arg("--notification_interval")
@cliutils.arg("--notification_period")
@cliutils.arg("--use", nargs='+')
@cliutils.arg("--name")
@cliutils.arg("--register")
@cliutils.arg("--check_interval")
@cliutils.arg("--retry_interval")
def do_config_host_update(sc, args):
    """Update a config host."""
    arg_names = ['host_name',
                 'address',
                 'max_check_attempts',
                 'check_period',
                 'contacts',
                 'contact_groups',
                 'custom_fields',
                 'notification_interval',
                 'notification_period',
                 'use',
                 'name',
                 'register',
                 'check_interval',
                 'retry_interval']
    host = _dict_from_args(args, arg_names)
    sc.config.hosts.update(args.original_host_name, host)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--address", help="Address of the host")
@cliutils.arg("--max_check_attempts")
@cliutils.arg("--check_period")
@cliutils.arg("--contacts", nargs='+')
@cliutils.arg("--contact_groups", nargs='+')
@cliutils.arg("--custom_fields")
@cliutils.arg("--notification_interval")
@cliutils.arg("--notification_period")
@cliutils.arg("--use", nargs='+')
@cliutils.arg("--name")
@cliutils.arg("--register")
@cliutils.arg("--check_interval")
@cliutils.arg("--retry_interval")
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
                 'use',
                 'name',
                 'register',
                 'check_interval',
                 'retry_interval']
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
            'notification_interval', 'notification_period', 'use',
            'name', 'register', 'check_interval', 'retry_interval'
        ]

        utils.print_item(host, hostProperties)


@cliutils.arg("--host_name", help="Name of the host")
def do_config_host_delete(sc, args):
    """Delete a config host."""
    sc.config.hosts.delete(args.host_name)


@cliutils.arg("--macromodulation_name", help="New name of the macromodulation")
@cliutils.arg("--modulation_period")
@cliutils.arg("--macros")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_macromodulation_list(sc, args):
    """List all config macromodulations."""
    arg_names = ['macromodulation_name',
                 'modulation_period',
                 'macros'
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    macromodulations = sc.config.macromodulations.list(lq)

    if args.json:
        print(utils.json_formatter(macromodulations))
    else:
        cols = [
            'macromodulation_name',
            'modulation_period',
            'macros'
        ]

        formatters = {
            'macromodulation_name': lambda x: x.get(
                'macromodulation_name', ''),
            'modulation_period': lambda x: x.get('modulation_period', ''),
            'macros': lambda x: x.get('macros', ''),
        }
        utils.print_list(macromodulations, cols, formatters=formatters)


@cliutils.arg("original_macromodulation_name",
              help="Original name of the macromodulation")
@cliutils.arg("--macromodulation_name", help="New name of the macromodulation")
@cliutils.arg("--modulation_period")
@cliutils.arg("--macros")
def do_config_macromodulation_update(sc, args):
    """Update a config macromodulation."""
    arg_names = ['macromodulation_name',
                 'modulation_period',
                 'macros']
    macromodulation = _dict_from_args(args, arg_names)
    sc.config.macromodulations.update(args.original_macromodulation_name,
                                      macromodulation)


@cliutils.arg("--macromodulation_name", help="Name of the macromodulation")
@cliutils.arg("--modulation_period")
@cliutils.arg("--macros")
def do_config_macromodulation_create(sc, args):
    """Create a config macromodulation."""
    arg_names = ['macromodulation_name',
                 'modulation_period',
                 'macros']
    macromodulation = _dict_from_args(args, arg_names)

    if "macros" in macromodulation:
        macromodulation["macros"] = json.loads(macromodulation["macros"])

    sc.config.macromodulations.create(**macromodulation)


@cliutils.arg("--macromodulation_name", help="Name of the macromodulation")
def do_config_macromodulation_show(sc, args):
    """Show a specific macromodulation."""
    macromodulation = sc.config.macromodulations.get(args.macromodulation_name)

    if args.json:
        print(utils.json_formatter(macromodulation))
    elif macromodulation:
        """ Specify the shown order and all the properties to display """
        macromodulationProperties = ['macromodulation_name',
                                     'modulation_period',
                                     'macros'
                                     ]

        utils.print_item(macromodulation, macromodulationProperties)


@cliutils.arg("--macromodulation_name", help="Name of the host")
def do_config_macromodulation_delete(sc, args):
    """Delete a config macromodulation."""
    sc.config.macromodulations.delete(args.macromodulation_name)


@cliutils.arg("--notificationway_name", help="New name of the notificationway")
@cliutils.arg("--host_notification_period")
@cliutils.arg("--service_notification_period")
@cliutils.arg("--host_notification_options", nargs='+')
@cliutils.arg("--service_notification_options", nargs='+')
@cliutils.arg("--host_notification_commands", nargs='+')
@cliutils.arg("--service_notification_commands", nargs='+')
@cliutils.arg("--min_business_impact")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_notificationway_list(sc, args):
    """List all config notificationways."""
    arg_names = ['notificationway_name',
                 'host_notification_period',
                 'service_notification_period',
                 'host_notification_options',
                 'service_notification_options',
                 'service_notification_commands',
                 'host_notification_commands',
                 'min_business_impact',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    notificationways = sc.config.notificationways.list(lq)

    if args.json:
        print(utils.json_formatter(notificationways))
    else:
        cols = [
            'notificationway_name',
            'host_notification_period',
            'service_notification_period',
            'host_notification_options',
            'service_notification_options',
            'service_notification_commands',
            'host_notification_commands'
        ]

        formatters = {
            'notificationway_name': lambda x: x.get(
                'notificationway_name', ''),
            'host_notification_period': lambda x: x.get(
                'host_notification_period', ''),
            'service_notification_period': lambda x: x.get(
                'service_notification_period', ''),
            'host_notification_options': lambda x: x.get(
                'host_notification_options', ''),
            'service_notification_options': lambda x: x.get(
                'service_notification_options', ''),
            'host_notification_commands': lambda x: x.get(
                'host_notification_commands', ''),
            'service_notification_commands': lambda x: x.get(
                'service_notification_commands', ''),
        }
        utils.print_list(notificationways, cols, formatters=formatters)


@cliutils.arg("original_notificationway_name",
              help="Original name of the notificationway")
@cliutils.arg("--notificationway_name", help="New name of the notificationway")
@cliutils.arg("--host_notification_period")
@cliutils.arg("--service_notification_period")
@cliutils.arg("--host_notification_options", nargs='+')
@cliutils.arg("--service_notification_options", nargs='+')
@cliutils.arg("--host_notification_commands", nargs='+')
@cliutils.arg("--service_notification_commands", nargs='+')
@cliutils.arg("--min_business_impact")
def do_config_notificationway_update(sc, args):
    """Update a config notificationway."""
    arg_names = ['notificationway_name',
                 'host_notification_period',
                 'service_notification_period',
                 'host_notification_options',
                 'service_notification_options',
                 'service_notification_commands',
                 'host_notification_commands',
                 'min_business_impact']
    notificationway = _dict_from_args(args, arg_names)
    sc.config.notificationways.update(args.original_notificationway_name,
                                      notificationway)


@cliutils.arg("--notificationway_name", help="Name of the notificationway")
@cliutils.arg("--host_notification_period")
@cliutils.arg("--service_notification_period")
@cliutils.arg("--host_notification_options", nargs='+')
@cliutils.arg("--service_notification_options", nargs='+')
@cliutils.arg("--host_notification_commands", nargs='+')
@cliutils.arg("--service_notification_commands", nargs='+')
@cliutils.arg("--min_business_impact")
def do_config_notificationway_create(sc, args):
    """Create a config notificationway."""
    arg_names = ['notificationway_name',
                 'host_notification_period',
                 'service_notification_period',
                 'host_notification_options',
                 'service_notification_options',
                 'service_notification_commands',
                 'host_notification_commands',
                 'min_business_impact']
    notificationway = _dict_from_args(args, arg_names)

    sc.config.notificationways.create(**notificationway)


@cliutils.arg("--notificationway_name", help="Name of the notificationway")
def do_config_notificationway_show(sc, args):
    """Show a specific notificationway."""
    notificationway = sc.config.notificationways.get(args.notificationway_name)

    if args.json:
        print(utils.json_formatter(notificationway))
    elif notificationway:
        """ Specify the shown order and all the properties to display """
        notificationwayProperties = [
            'notificationway_name',
            'host_notification_period',
            'service_notification_period',
            'host_notification_options',
            'service_notification_options',
            'service_notification_commands',
            'host_notification_commands',
            'min_business_impact'
        ]

        utils.print_item(notificationway, notificationwayProperties)


@cliutils.arg("--notificationway_name", help="Name of the notificationway")
def do_config_notificationway_delete(sc, args):
    """Delete a config notificationway."""
    sc.config.notificationways.delete(args.notificationway_name)


@cliutils.arg("--realm_name", help="New name of the realm")
@cliutils.arg("--realm_members", nargs='+')
@cliutils.arg("--default")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_realm_list(sc, args):
    """List all config realms."""
    arg_names = ['realm_name',
                 'realm_members',
                 'default',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    realms = sc.config.realms.list(lq)

    if args.json:
        print(utils.json_formatter(realms))
    else:
        cols = [
            'realm_name',
            'realm_members',
            'default'
        ]

        formatters = {
            'realm_name': lambda x: x.get('realm_name', ''),
            'realm_members': lambda x: x.get('realm_members', ''),
            'default': lambda x: x.get('default', '')
        }
        utils.print_list(realms, cols, formatters=formatters)


@cliutils.arg("original_realm_name", help="Original name of the realm")
@cliutils.arg("--realm_name", help="New name of the realm")
@cliutils.arg("--realm_members", nargs='+')
@cliutils.arg("--default")
def do_config_realm_update(sc, args):
    """Update a config realm."""
    arg_names = ['realm_name',
                 'realm_members',
                 'default']
    realm = _dict_from_args(args, arg_names)
    sc.config.realms.update(args.original_realm_name, realm)


@cliutils.arg("--realm_name", help="Name of the realm")
@cliutils.arg("--realm_members", nargs='+')
@cliutils.arg("--default")
def do_config_realm_create(sc, args):
    """Create a config realm."""
    arg_names = ['realm_name',
                 'realm_members',
                 'default']
    realm = _dict_from_args(args, arg_names)

    sc.config.realms.create(**realm)


@cliutils.arg("--realm_name", help="Name of the realm")
def do_config_realm_show(sc, args):
    """Show a specific realm."""
    realm = sc.config.realms.get(args.realm_name)

    if args.json:
        print(utils.json_formatter(realm))
    elif realm:
        """ Specify the shown order and all the properties to display """
        realmProperties = [
            'realm_name',
            'realm_members',
            'default'
        ]

        utils.print_item(realm, realmProperties)


@cliutils.arg("--realm_name", help="Name of the realm")
def do_config_realm_delete(sc, args):
    """Delete a config realm."""
    sc.config.realms.delete(args.realm_name)


@cliutils.arg("--servicegroup_name", help="New name of the service group")
@cliutils.arg("--members")
@cliutils.arg("--alias")
@cliutils.arg("--servicegroup_members")
@cliutils.arg("--notes")
@cliutils.arg("--notes_url")
@cliutils.arg("--action_url")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_servicegroup_list(sc, args):
    """List all config service groups."""
    arg_names = ['servicegroup_name',
                 'members',
                 'alias',
                 'servicegroup_members',
                 'notes',
                 'notes_url',
                 'action_url',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    servicegroups = sc.config.servicegroups.list(lq)

    if args.json:
        print(utils.json_formatter(servicegroups))
    else:
        cols = [
            'servicegroup_name',
            'members',
            'alias',
            'servicegroup_members',
            'notes',
            'notes_url',
            'action_url'
        ]

        formatters = {
            'servicegroup_name': lambda x: x.get('servicegroup_name', ''),
            'members': lambda x: x.get('members', ''),
            'alias': lambda x: x.get('alias', ''),
            'servicegroup_members': lambda x: x.get(
                'servicegroup_members', ''),
            'notes': lambda x: x.get('notes', ''),
            'notes_url': lambda x: x.get('notes_url', ''),
            'action_url': lambda x: x.get('action_url', '')
        }
        utils.print_list(servicegroups, cols, formatters=formatters)


@cliutils.arg("original_servicegroup_name",
              help="Original name of the service group")
@cliutils.arg("--servicegroup_name", help="New name of the service group")
@cliutils.arg("--members", nargs='+')
@cliutils.arg("--alias")
@cliutils.arg("--servicegroup_members", nargs='+')
@cliutils.arg("--notes")
@cliutils.arg("--notes_url")
@cliutils.arg("--action_url")
def do_config_servicegroup_update(sc, args):
    """Update a config service group."""
    arg_names = ['servicegroup_name',
                 'members',
                 'alias',
                 'servicegroup_members',
                 'notes',
                 'notes_url',
                 'action_url']
    servicegroup = _dict_from_args(args, arg_names)
    sc.config.servicegroups.update(args.original_servicegroup_name,
                                   servicegroup)


@cliutils.arg("--servicegroup_name", help="Name of the service group")
@cliutils.arg("--members", nargs='+')
@cliutils.arg("--alias")
@cliutils.arg("--servicegroup_members", nargs='+')
@cliutils.arg("--notes")
@cliutils.arg("--notes_url")
@cliutils.arg("--action_url")
def do_config_servicegroup_create(sc, args):
    """Create a config service group."""
    arg_names = ['servicegroup_name',
                 'members',
                 'alias',
                 'servicegroup_members',
                 'notes',
                 'notes_url',
                 'action_url']
    servicegroup = _dict_from_args(args, arg_names)

    sc.config.servicegroups.create(**servicegroup)


@cliutils.arg("--servicegroup_name", help="Name of the service group")
def do_config_servicegroup_show(sc, args):
    """Show a specific service group."""
    servicegroup = sc.config.servicegroups.get(args.servicegroup_name)
    if args.json:
        print(utils.json_formatter(servicegroup))
    elif servicegroup:
        """ Specify the shown order and all the properties to display """
        servicegroupProperties = ['servicegroup_name',
                                  'members',
                                  'alias',
                                  'servicegroup_members',
                                  'notes',
                                  'notes_url',
                                  'action_url'
                                  ]

        utils.print_item(servicegroup, servicegroupProperties)


@cliutils.arg("--servicegroup_name", help="Name of the service group")
def do_config_servicegroup_delete(sc, args):
    """Delete a config service group."""
    sc.config.servicegroups.delete(args.servicegroup_name)


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
@cliutils.arg("--use")
@cliutils.arg("--name")
@cliutils.arg("--register")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_service_list(sc, args):
    """List all config services."""
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
                 'use',
                 'name',
                 'register',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    services = sc.config.services.list(lq)

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


@cliutils.arg("--host_name", nargs='+')
@cliutils.arg("--service_description")
@cliutils.arg("--check_command")
@cliutils.arg("--max_check_attempts")
@cliutils.arg("--check_interval")
@cliutils.arg("--retry_interval")
@cliutils.arg("--check_period")
@cliutils.arg("--notification_interval")
@cliutils.arg("--notification_period")
@cliutils.arg("--contacts", nargs='+')
@cliutils.arg("--contact_groups", nargs='+')
@cliutils.arg("--passive_checks_enabled")
@cliutils.arg("--use", nargs='+')
@cliutils.arg("--name")
@cliutils.arg("--register")
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
                 'use',
                 'name',
                 'register']
    service = _dict_from_args(args, arg_names)
    sc.config.services.create(**service)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--service_description", help="The service_description")
def do_config_service_delete(sc, args):
    """Create a config service."""
    sc.config.services.delete(args.host_name,
                              args.service_description)


@cliutils.arg("--timeperiod_name", help="New name of the timeperiod")
@cliutils.arg("--exclude")
@cliutils.arg("--periods", nargs='+')
@cliutils.arg("--alias")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_config_timeperiod_list(sc, args):
    """List all config timeperiods."""
    arg_names = ['timeperiod_name',
                 'exclude',
                 'periods',
                 'alias',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    timeperiods = sc.config.timeperiods.list(lq)

    if args.json:
        print(utils.json_formatter(timeperiods))
    else:
        cols = [
            'timeperiod_name',
            'exclude',
            'periods'
        ]

        formatters = {
            'timeperiod_name': lambda x: x.get('timeperiod_name', ''),
            'exclude': lambda x: x.get('exclude', ''),
            'periods': lambda x: x.get('periods', '')
        }
        utils.print_list(timeperiods, cols, formatters=formatters)


@cliutils.arg("original_timeperiod_name",
              help="Original name of the timeperiod")
@cliutils.arg("--timeperiod_name", help="New name of the timeperiod")
@cliutils.arg("--exclude")
@cliutils.arg("--periods", nargs='+')
@cliutils.arg("--alias")
def do_config_timeperiod_update(sc, args):
    """Update a config timeperiod."""
    arg_names = ['timeperiod_name',
                 'exclude',
                 'periods',
                 'alias']
    timeperiod = _dict_from_args(args, arg_names)
    sc.config.timeperiods.update(args.original_timeperiod_name, timeperiod)


@cliutils.arg("--timeperiod_name", help="Name of the timeperiod")
@cliutils.arg("--exclude")
@cliutils.arg("--periods", nargs='+')
@cliutils.arg("--alias")
def do_config_timeperiod_create(sc, args):
    """Create a config timeperiod."""
    arg_names = ['timeperiod_name',
                 'exclude',
                 'periods',
                 'alias']
    timeperiod = _dict_from_args(args, arg_names)

    sc.config.timeperiods.create(**timeperiod)


@cliutils.arg("--timeperiod_name", help="Name of the timeperiod")
def do_config_timeperiod_show(sc, args):
    """Show a specific timeperiod."""
    timeperiod = sc.config.timeperiods.get(args.timeperiod_name)
    if args.json:
        print(utils.json_formatter(timeperiod))
    elif timeperiod:
        """ Specify the shown order and all the properties to display """
        timeperiodProperties = ['timeperiod_name',
                                'exclude',
                                'periods'
                                ]

        utils.print_item(timeperiod, timeperiodProperties)


@cliutils.arg("--timeperiod_name", help="Name of the timeperiod")
def do_config_timeperiod_delete(sc, args):
    """Delete a config timeperiod."""
    sc.config.timeperiods.delete(args.timeperiod_name)


def do_config_reload(sc, args):
    """Trigger a config reload."""
    print(sc.config.reload_config()['message'])


@cliutils.arg("--host_name", help="Host Name")
@cliutils.arg("--address", help="address")
@cliutils.arg("--state", help="state")
@cliutils.arg("--last_check", help="Last check")
@cliutils.arg("--last_state_change", help="Last state change")
@cliutils.arg("--long_output", help="Long output")
@cliutils.arg("--services", help="Services")
@cliutils.arg("--childs", help="childs")
@cliutils.arg("--parents", help="Parents")
@cliutils.arg("--description", help="description")
@cliutils.arg("--acknowledge", help="Acknowledge")
@cliutils.arg("--plugin_output", help="Plugin output")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_status_host_list(sc, args):
    """List all status hosts."""
    arg_names = ['host_name',
                 'address',
                 'state',
                 'last_check',
                 'last_state_change',
                 'long_output',
                 'description',
                 'acknowledged',
                 'plugin_output',
                 'services',
                 'childs',
                 'parents',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    services = sc.status.hosts.list(lq)

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


@cliutils.arg("--host_name", help="Host name")
@cliutils.arg("--service_description", help="Service description")
@cliutils.arg("--state", help="State")
@cliutils.arg("--last_check", help="Last check")
@cliutils.arg("--plugin_output", help="Plugin Output")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_status_service_list(sc, args):
    """List all status services."""

    arg_names = ['host_name',
                 'service_description',
                 'state',
                 'last_check',
                 'plugin_output',
                 'live_query',
                 'page_size',
                 'page'
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    services = sc.status.services.list(lq)

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
@cliutils.arg("--start_time", help="begin of the metric")
@cliutils.arg("--end_time", help="end of the metric")
@cliutils.arg("--service_description", help="Service description")
@cliutils.arg("--live_query", help="Live query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
def do_status_metrics_list(sc, args):
    """List all status metrics."""
    arg_names = ['host_name',
                 'metric_name',
                 'start_time',
                 'end_time',
                 'service_description',
                 'live_query',
                 'page_size',
                 'page',
                 ]
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    metrics = sc.status.hosts.metrics.list(lq)

    if args.json:
        print(utils.json_formatter(metrics))
    else:
        cols = utils.get_columns(metrics, [])
        formatters = reduce(_create_format, cols, {})

        utils.print_list(metrics, cols, formatters=formatters)


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--metric_name", help="Name of the metric")
@cliutils.arg("--service_description", help="Service description")
def do_status_metrics_show(sc, args):
    """Give the last status metrics."""
    arg_names = ['host_name',
                 'metric_name',
                 'service_description',
                 ]
    arg = _dict_from_args(args, arg_names)

    metrics = sc.status.hosts.metrics.get(**arg)
    if args.json:
        print(utils.json_formatter(metrics))
    else:
        if isinstance(metrics, dict):
            metrics = [metrics]

        cols = utils.get_columns(metrics,
                                 ['metric_name',
                                  ])
        formatters = reduce(_create_format, cols, {})

        utils.print_list(metrics, cols, formatters=formatters)


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


@cliutils.arg("--host_name", help="Name of the host")
@cliutils.arg("--service_description", help="Service description")
@cliutils.arg("--event_type", help="Event type")
@cliutils.arg("--start_time", help="Start of the event to query")
@cliutils.arg("--end_time", help="End of the event to query")
@cliutils.arg("--page_size", help="Number of returned data")
@cliutils.arg("--page", help="Page number")
@cliutils.arg("--live_query", help="A live query")
def do_status_events_list(sc, args):
    """List all events."""

    arg_names = ['host_name',
                 'service_description',
                 'event_type',
                 'start_time',
                 'end_time',
                 'page_size',
                 'page',
                 'live_query']
    arg_dict = _dict_from_args(args, arg_names)
    lq = utils.create_query(**arg_dict)
    events = sc.status.events.list(lq)

    if args.json:
        print(utils.json_formatter(events))
    else:
        cols = utils.get_columns(events,
                                 ['host_name',
                                  'service_description',
                                  'event_type'])

        formatters = reduce(_create_format, cols, {})

        utils.print_list(events, cols, formatters=formatters)


def _create_format(init, col):
    init[col] = lambda x: x.get(col, '')
    return init
