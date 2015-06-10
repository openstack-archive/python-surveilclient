# Copyright (c) 2013 OpenStack Foundation
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

import os
import prettytable

from surveilclient.openstack.common import importutils
from oslo.serialization import jsonutils


# Decorator for cli-args
def arg(*args, **kwargs):
    def _decorator(func):
        # Because of the semantics of decorator composition if we just append
        #  to the options list positional options will appear to be backwards.
        func.__dict__.setdefault('arguments', []).insert(0, (args, kwargs))
        return func
    return _decorator


def env(*vars, **kwargs):
    """
    returns the first environment variable set
    if none are non-empty, defaults to '' or keyword arg default
    """
    for v in vars:
        value = os.environ.get(v, None)
        if value:
            return value
    return kwargs.get('default', '')


def import_versioned_module(version, submodule=None):
    module = 'surveilclient.v%s' % version
    if submodule:
        module = '.'.join((module, submodule))
    return importutils.import_module(module)


def json_formatter(js):
    return jsonutils.dumps(js, indent=2, ensure_ascii=False)


def print_item(objs, properties):
    """ Add the missing properties to the objs """
    for prop in properties:
        if prop not in objs:
            objs[prop] = ""

    cols = [
        'Property',
        'Value'
    ]

    """ Override the properties keys pass in parameter """

    len_property_max=0
    for property in properties:
        if len(property) > len_property_max:
            len_property_max = len(property)

    # 80 char per line - 7 char (space or | )
    len_available = 73 - len_property_max
    list = []

    for property in properties:
        val_lines = []
        for i in range(0, len(objs[property].__str__()), len_available):
            val_lines.append(objs[property].__str__()[i:i+len_available])

        val_lines ='\n'.join(val_lines)
        list.append({'prop': property, 'value': val_lines})

    formatters = {
        'Property': lambda x: x.get('prop', ''),
        'Value': lambda x: x.get('value', ''),
    }

    print_list(list, cols, formatters=formatters)


def print_list(objs, fields, field_labels=None, formatters={}, sortby=None):
    field_labels = field_labels or fields
    pt = prettytable.PrettyTable([f for f in field_labels],
                                 caching=False, print_empty=False)
    pt.align = 'l'

    for o in objs:
        row = []
        for field in fields:
            if field in formatters:
                row.append(formatters[field](o))
            else:
                data = getattr(o, field, None) or ''
                row.append(data)
        pt.add_row(row)
    if sortby is None:
        print(pt.get_string())
    else:
        print(pt.get_string(sortby=field_labels[sortby]))
