# Copyright 2014 - Savoir-Faire Linux inc.
# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
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

"""
Command-line interface to the surveil API.
"""

from __future__ import print_function

from surveilclient import client as surveil_client
from surveilclient.common import utils
from surveilclient import exc

import argparse
import sys


class SurveilShell(object):

    default_api_version = '2_0'

    def __init__(self):
        self.parser = self.get_base_parser()

    def get_base_parser(self):
        parser = argparse.ArgumentParser(
            prog='surveil',
            description=__doc__.strip(),
            epilog='See "surveil help COMMAND" '
                   'for help on a specific command.',
            add_help=False,
            formatter_class=HelpFormatter,
        )

        parser.add_argument('-h', '--help', action='store_true')

        parser.add_argument('--surveil-api-url',
                            default=utils.env(
                                'SURVEIL_API_URL',
                                default='http://localhost:8080/v2'),
                            help='Defaults to env[SURVEIL_API_URL].')

        parser.add_argument('--surveil-api-version',
                            default=utils.env(
                                'SURVEIL_API_VERSION',
                                default=self.default_api_version),
                            help='Defaults to env[SURVEIL_API_VERSION] or %s' %
                                 self.default_api_version)

        parser.add_argument('-j', '--json',
                            action='store_true',
                            help='output raw json response')

        return parser

    def get_subcommand_parser(self, version=default_api_version):
        parser = self.get_base_parser()
        self.subcommands = {}
        subparsers = parser.add_subparsers(metavar='<subcommand>',
                                           dest='subcommand')
        submodule = utils.import_versioned_module(version, 'shell')
        self._find_actions(subparsers, submodule)
        self._find_actions(subparsers, self)
        self._add_bash_completion_subparser(subparsers)
        self.parser = parser
        return parser

    def _add_bash_completion_subparser(self, subparsers):
        subparser = subparsers.add_parser(
            'bash_completion',
            add_help=False,
            formatter_class=HelpFormatter
        )
        self.subcommands['bash_completion'] = subparser
        subparser.set_defaults(func=self.do_bash_completion)

    def _find_actions(self, subparsers, actions_module):
        for attr in (a for a in dir(actions_module) if a.startswith('do_')):
            # I prefer to be hyphen-separated instead of underscores.
            command = attr[3:].replace('_', '-')
            callback = getattr(actions_module, attr)
            desc = callback.__doc__ or ''
            help = desc.strip().split('\n')[0]
            arguments = getattr(callback, 'arguments', [])

            subparser = subparsers.add_parser(command,
                                              help=help,
                                              description=desc,
                                              formatter_class=HelpFormatter)
            self.subcommands[command] = subparser
            for (args, kwargs) in arguments:
                subparser.add_argument(*args, **kwargs)
            subparser.set_defaults(func=callback)

    @utils.arg('command', metavar='<subcommand>', nargs='?',
               help='Display help for <subcommand>.')
    def do_help(self, args=None):
        """Display help about this program or one of its subcommands."""
        if getattr(args, 'command', None):
            if args.command in self.subcommands:
                self.subcommands[args.command].print_help()
            else:
                raise exc.CommandError("'%s' is not a valid subcommand" %
                                       args.command)
        else:
            self.parser.print_help()

    def do_bash_completion(self, args):
        """Prints all of the commands and options to stdout.

        The surveil.bash_completion script doesn't have to hard code them.
        """
        commands = set()
        options = set()
        for sc_str, sc in self.subcommands.items():
            commands.add(sc_str)
            for option in list(sc._optionals._option_string_actions):
                options.add(option)

        commands.remove('bash-completion')
        commands.remove('bash_completion')
        print(' '.join(commands | options))

    def main(self, argv):

        cfg, args = self.parser.parse_known_args(argv)

        parser = self.get_subcommand_parser(cfg.surveil_api_version)
        if not argv or (cfg.help and not args):
            self.do_help()
            return 0

        cfg = parser.parse_args(argv)
        if cfg.help or cfg.func == self.do_help:
            self.do_help(cfg)
            return 0

        if cfg.func == self.do_bash_completion:
            self.do_bash_completion(cfg)
            return 0

        endpoint = cfg.surveil_api_url
        if not endpoint:
            raise exc.CommandError("you must specify a Surveil API URL"
                                   " via either --surveil-api-url or"
                                   " env[SURVEIL_API_URL]")
        client = surveil_client.Client(endpoint,
                                       version=cfg.surveil_api_version)
        return cfg.func(client, cfg)


class HelpFormatter(argparse.HelpFormatter):
    def start_section(self, heading):
        # Title-case the headings
        heading = '%s%s' % (heading[0].upper(), heading[1:])
        super(HelpFormatter, self).start_section(heading)


def main():
    try:
        SurveilShell().main(sys.argv[1:])
    except exc.CommandError as err:
        print(err, file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("... terminating surveil client", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        import traceback
        print(str(e), file=sys.stderr)
        print(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
