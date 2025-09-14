from flask_sqlalchemy import SQLAlchemy
import datetime
from app.extensions import db

class Sitemaps(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    sitemap_no = db.Column(db.Integer,nullable=False)
    url = db.Column(db.String(255),nullable=False)
    is_scraped = db.Column(db.Boolean,nullable=False)
    updated_at = db.Column(db.DateTime,default=datetime.datetime.now())