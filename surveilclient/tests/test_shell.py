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

import sys
import unittest

from mox3 import mox
import six

from surveilclient.common import http
from surveilclient import exc
from surveilclient import shell as surveil_shell


class ShellBase(unittest.TestCase):

    def setUp(self):
        super(ShellBase, self).setUp()
        self.m = mox.Mox()
        self.m.StubOutWithMock(http.HTTPClient, 'json_request')
        self.addCleanup(self.m.VerifyAll)
        self.addCleanup(self.m.UnsetStubs)

        # Some tests set exc.verbose = 1, so reset on cleanup
        def unset_exc_verbose():
            exc.verbose = 0

        self.addCleanup(unset_exc_verbose)

    def shell(self, argstr):
        orig = sys.stdout
        try:
            sys.stdout = six.StringIO()
            _shell = surveil_shell.SurveilShell()
            _shell.main(argstr.split())
            self.subcommands = _shell.subcommands.keys()
        except SystemExit:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.assertEqual(0, exc_value.code)
        finally:
            out = sys.stdout.getvalue()
            sys.stdout.close()
            sys.stdout = orig

        return out


class ShellTest(ShellBase):
    def test_help_unknown_command(self):
        self.assertRaises(exc.CommandError, self.shell, 'help foofoo')

    def test_help(self):
        required = [
            '^usage: surveil',
            '(?m)^See "surveil help COMMAND" for help on a specific command',
        ]
        help_text = self.shell('help')
        for r in required:
            self.assertRegexpMatches(help_text, r)

    def test_help_on_subcommand(self):
        required = [
            '^usage: surveil config-host-list',
            "(?m)^List all config hosts.",
        ]
        argstrings = [
            'help config-host-list',
        ]
        for argstr in argstrings:
            help_text = self.shell(argstr)
            for r in required:
                self.assertRegexpMatches(help_text, r)
