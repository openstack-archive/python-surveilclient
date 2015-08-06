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

import requests_mock

from surveilclient.tests.v2_0 import clienttest


class TestCommands(clienttest.ClientTest):

    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/commands",
                   text='[{"command_name":"myCommand"}]'
                   )

            self.assertEqual(
                self.client.config.commands.list(),
                [{"command_name": "myCommand"}]
            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/commands",
                  text='{"command_name": "new_command", "command_line": "new_line"}'
                  )

            self.client.config.commands.create(
                command_name="new_command",
                command_line="new_line"
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "command_name": "new_command",
                    "command_line": "new_line"
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get("http://localhost:5311/v2/config/commands/command_to_show",
                  text='{"command_name": "command_to_show",'
                       '"command_line": "line"}'
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

    def test_update(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/commands/command_to_update",
                  text='{"command_line": "updated command_line"}'
                  )

            self.client.config.commands.update(
                command_name="command_to_update",
                command={'command_line': "updated command_line"}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "command_line": "updated command_line"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/commands/"
                     "command_to_delete",
                     text="body"
                     )

            body = self.client.config.commands.delete(
                command_name="command_to_delete",
            )

            self.assertEqual(
                body,
                "body"
            )
