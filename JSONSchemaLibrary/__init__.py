import os
from robot.api import logger

import jsonschema
import json


class JSONSchemaLibrary(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self, schema_location='schemas'):
        self._schema_location = schema_location
        if not self._schema_location.endswith('/'):
            self._schema_location = '{}/'.format(self._schema_location)

    def validate_json(self, schema_path, data):
        schema = self._load_schema(schema_path)
        try:
            jsonschema.validate(data, schema)
        except jsonschema.ValidationError as e:
            logger.debug(e)
            err_msg = 'Validation error for schema {}: {}'.format(
                schema_path, e.message)
            raise jsonschema.ValidationError(err_msg)

    def _load_schema(self, schema_path):
        if os.path.isfile(schema_path):
            schema_file = schema_path
        else:
            schema_file = '{}/{}'.format(self._schema_location, schema_path)
            if not os.path.isfile(schema_file):
                raise FileNotFoundError(
                    'Schema file not found: {}'.format(schema_path))
        schema = json.loads(open(schema_file).read())
        return schema
