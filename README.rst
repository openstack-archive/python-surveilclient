Python bindings to the Surveil API
==================================

This is a client library for Surveil built on the Surveil API.


Python API
----------

To use the python API, simply create a client with the endpoint::

    from surveilclient.v1_0 import client
    c = client.Client('http://localhost:8080/v1')
    hosts = c.hosts.list()

