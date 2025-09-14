from flask_sqlalchemy import SQLAlchemy
from app.extensions import db

class BbbCompanies(db.Model):
    __tablename__ = 'bbb_companies'
    id = db.Column(db.Integer,primary_key=True)
    business_name = db.Column(db.String)
    website = db.Column(db.String)
    phone = db.Column(db.String)
    incorporated = db.Column(db.DateTime)
    management = db.Column(db.String)
    business_categories = db.Column(db.String)
    address = db.Column(db.String)
    sitemap_url = db.Column(db.String)
    sitemap_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
