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

import unittest

import mock

from surveilclient import client


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = client.Client('http://localhost:8080/v2',
                                    auth_url='http://localhost:8080/v2/auth',
                                    version='2_0')

        #  Mock the _get_auth_token call
        self.client.http_client._get_auth_token = mock.Mock(
            return_value="IAMAFAKETOKEN"
        )
