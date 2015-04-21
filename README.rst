Python bindings to the Surveil API
==================================

This is a client library for Surveil built on the Surveil API.

Command-line API
----------------

Installing this package gets you a shell command, ``surveil``, that you
can use to interact with the Surveil API.

You'll need to provide the Surveil API URL. You can do this with the
``--surveil-api-url`` parameter, but it's easier to just set it as environment
variable::

    export SURVEIL_API_URL=http://localhost:8080/v2

You'll find complete documentation on the shell by running ``surveil help``.

Bash completion
~~~~~~~~~~~~~~~

Basic command tab completion can be enabled by sourcing the bash completion script::

    source /usr/local/share/monasca.bash_completion

Python API
----------

To use the python API, simply create a client with the endpoint::

    from surveilclient import client
    c = client.Client('http://localhost:8080/v2', version='2_0')
    hosts = c.config.hosts.list()

