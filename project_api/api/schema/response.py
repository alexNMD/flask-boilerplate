from marshmallow import Schema, fields


class AbstractResponseSchema(Schema):
    status = fields.Str()
    message = fields.Str()
    data = fields.Raw(allow_none=True)


class ErrorResponseSchema(AbstractResponseSchema):
    pass


class CreatedResponseSchema(AbstractResponseSchema):
    pass


class OkResponseSchema(AbstractResponseSchema):
    pass
