from flask import Blueprint, jsonify, current_app, request
from app.models.Sitemaps import Sitemaps
from app.models.Bbb_companies import BbbCompanies
from app.schemas.data_schema import Companies_Schema
from app.schemas.data_schema import Sitemaps as Sitemap_schema
from app.extensions import ma, jwt
from flask_jwt_extended import jwt_required, get_jwt_identity

data_bp = Blueprint('data_bp',__name__)

@data_bp.route('/get_sitemaps',methods=['Get'])
@jwt_required()
def get_sitemaps():
    max_value = 10
    current = request.args.get('page',1,type=int)
    current = min(current,max_value)

    per_page = request.args.get('per_page',10,type=int)
    per_page = min(per_page,max_value)

    results = Sitemaps.query.paginate(page=current,per_page=per_page,error_out=False)
    myschema = Sitemap_schema(many=True)
    new_results = myschema.dump(results.items)

    return new_results

@data_bp.route('/get_companies',methods=['Get'])
@jwt_required()
def get_companies():

    max_value = 10
    current = request.args.get('page',1,type=int)
    current = min(current,max_value)

    per_page = request.args.get('per_page',10,type=int)
    per_page = min(per_page,max_value)

    results = BbbCompanies.query.paginate(page=current,per_page=per_page,error_out=False)
    myschema = Companies_Schema(many=True)
    new_results = myschema.dump(results.items)

    return new_results