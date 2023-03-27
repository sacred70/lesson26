from marshmallow import Schema, fields, validates_schema, ValidationError
# проверка на правильность команд от пользователя
# список дозволенных команд

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'sort')


class RequestSchema(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" нет такой команды')


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestSchema(), many=True)
