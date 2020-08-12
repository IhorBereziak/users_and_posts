from marshmallow import Schema, fields
from marshmallow.validate import Length


class PostSchema(Schema):
    id = fields.Integer()
    text = fields.String(required=True, validate=Length(min=1, max=500))
    user_id = fields.Integer()
