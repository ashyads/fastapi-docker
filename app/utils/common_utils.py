from jsonschema import validate, ValidationError


def json_schema_validate(instance_data, schema):
    def json_schema_validate_inner_func(requested_data, json_validator_schema):
        try:
            validate(instance=requested_data, schema=json_validator_schema)
        except ValidationError as error:
            if requested_data is not None:
                for x in json_validator_schema.get('required'):
                    if x not in requested_data:
                        return f"{x}, Field Is Required"
            else:
                return f"{json_validator_schema.get('required')[0]}, Field Is Required"
            keyword = error.path[0] if len(error.path) > 0 else ""
            return f"{keyword} : {error.message}"

    not_valid = json_schema_validate_inner_func(instance_data, schema)
    if not_valid:
        raise Exception(not_valid)
    else:
        return None
