from flask_sqlalchemy import SQLAlchemy
import bcrypt
from app.extensions import db

class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,nullable=False)
    password = db.Column(db.String(255),nullable = False)

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
