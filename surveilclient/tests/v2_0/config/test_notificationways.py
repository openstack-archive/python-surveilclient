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


class TestNotificationWays(clienttest.ClientTest):
    def test_list(self):
        with requests_mock.mock() as m:
            m.post("http://localhost:5311/v2/config/notificationways",
                   text='[{'
                        '"notificationway_name": "email_in_day",'
                        '"host_notification_period": "24x7",'
                        '"service_notification_period": "24x7",'
                        '"host_notification_options": "d,u",'
                        '"service_notification_options": "w,c,r",'
                        '"host_notification_commands": "notify-service",'
                        '"service_notification_commands": "notify-host"'
                        '},'
                        '{'
                        '"notificationway_name": "email_all_time",'
                        '"host_notification_period": "24x7",'
                        '"service_notification_period": "24x7",'
                        '"host_notification_options": "d,r,f,u",'
                        '"service_notification_options": "w,f,c,r",'
                        '"host_notification_commands": "notify-service",'
                        '"service_notification_commands": "notify-host",'
                        '"min_business_impact": 5'
                        '}'
                        ']')

            notificationways = self.client.config.notificationways.list()

            self.assertEqual(
                notificationways,
                [
                    {
                        'notificationway_name': 'email_in_day',
                        'host_notification_period': '24x7',
                        'service_notification_period': '24x7',
                        'host_notification_options': 'd,u',
                        'service_notification_options': 'w,c,r',
                        'host_notification_commands': 'notify-service',
                        'service_notification_commands': 'notify-host'
                    },
                    {
                        'notificationway_name': 'email_all_time',
                        'host_notification_period': '24x7',
                        'service_notification_period': '24x7',
                        'host_notification_options': 'd,r,f,u',
                        'service_notification_options': 'w,f,c,r',
                        'host_notification_commands': 'notify-service',
                        'service_notification_commands': 'notify-host',
                        'min_business_impact': 5
                    }
                ]

            )

    def test_create(self):
        with requests_mock.mock() as m:
            m.put("http://localhost:5311/v2/config/notificationways",
                  text='{'
                       '"notificationway_name": "email_in_day",'
                       '"host_notification_period": "24x7",'
                       '"service_notification_period": "24x7",'
                       '"host_notification_options": "d,u",'
                       '"service_notification_options": "w,c,r",'
                       '"host_notification_commands": "notify-service",'
                       '"service_notification_commands": "notify-host"'
                       '}')

            self.client.config.notificationways.create(
                notificationway_name='test_create_notification',
                host_notification_period='24x7',
                service_notification_period='24x7',
                host_notification_options='d,r,f,u',
                service_notification_options='w,f,c,r',
                host_notification_commands='notify-service',
                service_notification_commands='notify-host',
                min_business_impact=5
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    'notificationway_name': 'test_create_notification',
                    'host_notification_period': '24x7',
                    'service_notification_period': '24x7',
                    'host_notification_options': 'd,r,f,u',
                    'service_notification_options': 'w,f,c,r',
                    'host_notification_commands': 'notify-service',
                    'service_notification_commands': 'notify-host',
                    'min_business_impact': 5
                }
            )

    def test_get(self):
        with requests_mock.mock() as m:
            m.get('http://localhost:5311/v2/config/'
                  'notificationways/email_all_time',
                  text='{'
                       '"notificationway_name": "email_all_time",'
                       '"host_notification_period": "24x7",'
                       '"service_notification_period": "24x7",'
                       '"host_notification_options": "d,r,f,u",'
                       '"service_notification_options": "w,f,c,r",'
                       '"host_notification_commands": "notify-service",'
                       '"service_notification_commands": "notify-host",'
                       '"min_business_impact": 5'
                       '}')

            notificationway = self.client.config.notificationways.get(
                notificationway_name='email_all_time'
            )

            self.assertEqual(
                notificationway,
                {
                    'notificationway_name': 'email_all_time',
                    'host_notification_period': '24x7',
                    'service_notification_period': '24x7',
                    'host_notification_options': 'd,r,f,u',
                    'service_notification_options': 'w,f,c,r',
                    'host_notification_commands': 'notify-service',
                    'service_notification_commands': 'notify-host',
                    'min_business_impact': 5
                }
            )

    def test_update(self):
        with requests_mock.mock() as m:
            m.put('http://localhost:5311/v2/'
                  'config/notificationways/email_all_time',
                  text='{"test": "test"}')

            self.client.config.notificationways.update(
                notificationway_name="email_all_time",
                notificationway={"host_notification_period": "updated"}
            )

            self.assertEqual(
                json.loads(m.last_request.body),
                {
                    "host_notification_period": u"updated"
                }
            )

    def test_delete(self):
        with requests_mock.mock() as m:
            m.delete("http://localhost:5311/v2/config/notificationways/bob",
                     text="body")

            body = self.client.config.notificationways.delete(
                notificationway_name="bob",
            )

            self.assertEqual(
                body,
                "body"
            )
