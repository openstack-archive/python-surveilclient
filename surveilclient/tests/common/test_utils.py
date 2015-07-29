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

import json
import unittest

from surveilclient.common import utils


class TestQuery(unittest.TestCase):

    def test_create_live_query(self):
        expected = {"filters": '{"is": {"host_name": ["toto"]}}',
                    "paging": {"page": 15}}
        args = {
            "live_query": '{"filters":{"is":{"host_name":["toto"]}},'
                          '"paging":{"page":15}}'
        }
        result = utils.create_query(**args)

        self.assertEqual(json.loads(result["filters"]),
                         json.loads(expected["filters"]))
        self.assertEqual(result["paging"], expected["paging"])

    def test_add_filters_to_live_query(self):
        expected = {"filters": '{"is": {"register": ["0"], '
                               '"host_name": ["toto"]}}',
                    "paging": {"page_size": 15}}
        args = {
            "live_query": '{"filters":{"is":{"host_name":["toto"]}},'
                          '"paging":{"page":10}}',
            "register": "0",
            "page_size": 15
        }
        result = utils.create_query(**args)

        self.assertEqual(json.loads(result["filters"]),
                         json.loads(expected["filters"]))
        self.assertEqual(result["paging"], expected["paging"])
