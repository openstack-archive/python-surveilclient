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

import unittest

from surveilclient import client
from surveilclient.v1_0 import client as v1_0_client
from surveilclient.v2_0 import client as v2_0_client


class TestClient(unittest.TestCase):

    def test_client_default_version(self):
        sc = client.Client('http://localhost:8080/sdf',
                           auth_url='http://localhost:8080/v2/auth')
        self.assertTrue(isinstance(sc, v2_0_client.Client))

    def test_client_init_v1(self):
        sc = client.Client('http://localhost:8080/v1', version='1_0')
        self.assertTrue(isinstance(sc, v1_0_client.Client))

    def test_client_init_v2(self):
        sc = client.Client('http://localhost:8080/v2',
                           auth_url='http://localhost:8080/v2/auth',
                           version='2_0')
        self.assertTrue(isinstance(sc, v2_0_client.Client))
