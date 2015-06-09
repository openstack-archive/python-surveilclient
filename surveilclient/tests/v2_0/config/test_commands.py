# Copyright 2015 - Savoir-Faire Linux inc.
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

import httpretty

from surveilclient.tests.v2_0 import clienttest


class TestCommands(clienttest.ClientTest):

    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.GET,
            "http://localhost:8080/v2/config/commands",
            body='[{"command_name":"myCommand"}]'
            )

        self.assertEqual(
            self.client.config.commands.list(),
            [{"command_name": "myCommand"}]
        )

    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:8080/v2/config/commands",
            body='{"command_name": "new_command", "command_line": "new_line"}'
        )

        self.client.config.commands.create(
            command_name="new_command",
            command_line="new_line"
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "command_name": "new_command",
                "command_line": "new_line"
            }
        )

    @httpretty.activate
    def test_show(self):
        httpretty.register_uri(
            httpretty.GET,
            "http://localhost:8080/v2/config/commands/command_to_show",
            body='{"command_name": "command_to_show", "command_line": "line"}'
        )

        command = self.client.config.commands.get(
            command_name="command_to_show"
        )

        self.assertEqual(
            command,
            {
                "command_name": "command_to_show",
                "command_line": "line"
            }
        )

    @httpretty.activate
    def test_update(self):
        httpretty.register_uri(
            httpretty.PUT,
            "http://localhost:8080/v2/config/commands/command_to_update",
            body='{"command_line": "updated command_line"}'
        )

        self.client.config.commands.update(
            command_name="command_to_update",
            command_line="updated command_line"
        )

        self.assertEqual(
            json.loads(httpretty.last_request().body.decode()),
            {
                "command_name": "command_to_update",
                "command_line": "updated command_line"
            }
        )

    @httpretty.activate
    def test_delete(self):
        httpretty.register_uri(
            httpretty.DELETE,
            "http://localhost:8080/v2/config/commands/command_to_delete",
            body="body"
        )

        body = self.client.config.commands.delete(
            command_name="command_to_delete",
        )

        self.assertEqual(
            body,
            "body"
        )
