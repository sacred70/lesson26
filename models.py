from marshmallow import Schema, fields, validate
# проверка на правильность команд от пользователя
# список дозволенных команд

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'sort', 'regex')


class RequestSchema(Schema):
    # проверяем есть ли данная команда в списке
    cmd1 = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value2 = fields.Str(required=True)
    file_name = fields.Str(required=True)




