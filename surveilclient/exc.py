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


class CommandError(BaseException):
    """Invalid usage of CLI."""


class ClientException(Exception):
    """The base exception class for all exceptions this library raises."""
    pass


class HttpError(ClientException):
    """The base exception class for all HTTP exceptions."""
    http_status = 0
    message = "HTTP Error"

    def __init__(self, message=None, details=None,
                 response=None, request_id=None,
                 url=None, method=None, http_status=None):
        self.http_status = http_status or self.http_status
        self.message = message or self.message
        self.details = details
        self.request_id = request_id
        self.response = response
        self.url = url
        self.method = method
        formatted_string = "%s (HTTP %s)" % (self.message, self.http_status)
        if request_id:
            formatted_string += " (Request-ID: %s)" % request_id
        super(HttpError, self).__init__(formatted_string)


def from_response(response, body, method, url):
    """Returns an instance of :class:`HttpError` or subclass based on response.

    :param response: instance of `requests.Response` class
    :param method: HTTP method used for request
    :param url: URL used for request
    """

    if response.getheader('Content-Type').startswith('application/json'):
        try:
            loaded_body = json.loads(body)
            if 'faultstring' in loaded_body:
                body = loaded_body['faultstring']
        except ValueError:
            pass

    return HttpError(
        response=response,
        url=url,
        method=method,
        http_status=response.status,
        message=body
    )