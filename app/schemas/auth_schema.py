from marshmallow import Schema, fields, validate
from app.extensions import ma

class LoginSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True,validate=validate.Length(min=6),error_messages={"required":"Password is required."})
