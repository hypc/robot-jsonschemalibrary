================================
RobotFramework JSONSchamaLibrary
================================

Provides a simple interface to `jsonschema`_, the Python implementation of JSON Schema.

Usage
-----

You can import library like this::

    Library     JSONSchemaLibrary

or::

    Library     JSONSchemaLibrary  /path/to/schemas

and you can write your testcase like this::

    My Test Case:
        Validate Json   schema_name.schema.json  {"foo": "bar"}

    My Test Case2:
        Validate Json   /path/to/schema_name.schema.json  {"foo": "bar"}

.. _`jsonschema`: https://github.com/Julian/jsonschema
