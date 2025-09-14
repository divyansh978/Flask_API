from flask import Blueprint, request, jsonify, current_app
from app.models.Users import Users
from app.schemas.auth_schema import LoginSchema
from flask_jwt_extended import create_access_token
from datetime import datetime, timedelta

auth_bp = Blueprint('auth_bp', __name__)
schema = LoginSchema()

@auth_bp.route('/login', methods=['Get','Post'])
def get_entries():
    data = request.get_json()

    if not data:
        return jsonify({'error': "Missing JSON payload"}), 400

    errors = schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400
    
    email = data['email']
    password = data['password']

    user = Users.query.filter_by(email=email).first()
    if user and user.check_password(password):
        # return the jwt token now
        token = create_access_token(identity=str(user.id),expires_delta=timedelta(hours=1))
        return {'token':token}
    else:
        return {'msg':'wrong credentials'}