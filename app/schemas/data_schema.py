from marshmallow import Schema, fields
from app.extensions import ma

class Companies_Schema(ma.Schema):
    id = fields.Int()
    business_name = fields.Str()
    website = fields.Str()
    phone = fields.Str()
    entity_type = fields.Str()
    management = fields.Str()
    business_categories = fields.Str()
    address = fields.Str()
    created_at = fields.DateTime(format="%d-%m-%Y")
    sitemap_id = fields.Int()

class Sitemaps(ma.Schema):
    id = fields.Int()
    sitemap_no = fields.Int()
    url = fields.Url()
    is_scraped = fields.Bool()
    updated_at = fields.DateTime(format="%d-%m-%Y")