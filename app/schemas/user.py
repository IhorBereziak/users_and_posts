from marshmallow import Schema, fields
from marshmallow.validate import Length, Regexp

from app.enums.regexp import regexp


class UserSchema(Schema):
    class Meta:
        load_only = ('password',)

    id = fields.Integer()
    email = fields.Email(required=True, validate=Length(max=40))
    password = fields.String(required=True, validate=Regexp(
        regexp.password, error='min 8, max 20, 1 uppercase, 1 digit, 1 special char'
    ))
    name = fields.String(required=True, validate=Regexp(
        regexp.name, error='Name must be only a-z and min 2, max 20 characters'
    ))

class UserUpdateSchema(Schema):
    id = fields.Integer()
    email = fields.Email(validate=Length(max=40))
    password = fields.String(validate=Regexp(
        regexp.password, error='min 8, max 20, 1 uppercase, 1 digit, 1 special char'
    ))
    name = fields.String(validate=Regexp(
        regexp.name, error='Name must be only a-z and min 2, max 20 characters'
    ))



