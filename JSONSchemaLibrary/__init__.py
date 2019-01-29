import os
from robot.api import logger

import jsonschema
import json


class JSONSchemaLibrary(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self, schema_locations='schemas'):
        if isinstance(schema_locations, str):
            schema_locations = (schema_locations,)
        elif isinstance(schema_locations, (list, tuple)):
            schema_locations = schema_locations
        else:
            schema_locations = ('schemas',)

        self._schema_locations = schema_locations

    def validate_json(self, schema='', data=None):
        if isinstance(schema, dict):
            schema = schema
        elif isinstance(schema, str) and schema != '':
            schema = self._load_schema(schema)
        else:
            raise jsonschema.SchemaError('No Schema')
        try:
            jsonschema.validate(data, schema)
        except jsonschema.ValidationError as e:
            logger.debug(e)
            err_msg = 'Validation error for schema {}: {}'.format(
                schema, e.message)
            raise jsonschema.ValidationError(err_msg)

    def _load_schema(self, schema_path):
        if os.path.isfile(schema_path):
            return json.loads(open(schema_path).read())

        for loc in self._schema_locations:
            schema_file = '{}/{}'.format(loc, schema_path)
            if os.path.isfile(schema_file):
                return json.loads(open(schema_file).read())

        raise FileNotFoundError(
            'Schema file not found: {}'.format(schema_path))
