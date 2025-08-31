from marshmallow import Schema, fields


class AuthLoginSchema(Schema):
    name = fields.Str(required=True)
    password = fields.Str(required=True)


class AuthTokenSchema(Schema):
    token = fields.Str()
