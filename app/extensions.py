from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import current_app
from flask_jwt_extended import JWTManager

jwt = JWTManager()

db = SQLAlchemy()
ma = Marshmallow()