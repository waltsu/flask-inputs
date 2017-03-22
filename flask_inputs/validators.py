
import jsonschema
from wtforms.validators import ValidationError


class JsonSchema(object):
    def __init__(self, schema, message=None):
        """Helper class for JSON validation using jsonschema.

        :param schema: JSON schema to validate against.
        :param message: Error message to return. Defaults to jsonschema's errors.

        :raises: wtforms.validators.ValidationError
        """
        self.schema = schema
        self.message = message

    def __call__(self, form, field):
        try:
            jsonschema.validate(field.data, self.schema)
        except jsonschema.ValidationError as e:
            if self.message:
                raise ValidationError(self.message)

            raise ValidationError(e.message)


class InputsValidator(object):
    def __init__(self, validator_class):
        """Takes Inputs-instance that'll validate the given field.

        This is useful when you want to validate e.g. nested objects with different Inputs-instances
        """
        self.validator_class = validator_class

    def __call__(self, form, field):
        validator = self.validator_class(field.data)
        if not validator.validate():
            raise ValidationError(validator.errors)
