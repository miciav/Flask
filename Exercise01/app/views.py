from flask import Blueprint, request, make_response
from flask_restful import Api, Resource
from sqlalchemy.exc import SQLAlchemyError

from app.http_status import HttpStatus
from app.model import User, db
from app.schemas import UserSchema

api_blueprint = Blueprint('api', __name__)
routes = Api(api_blueprint)
user_schema = UserSchema()


class UserResource(Resource):
    def get(self, id):
        user = User.query.get_or_404(id)
        dumped_user = user_schema.dump(user)
        return dumped_user

    def post(self):
        user_dict = request.get_json()
        if not user_dict:
            response = {'message': 'No input data provided'}
            return response, HttpStatus.bad_request_400.value
        errors = user_schema.validate(user_dict)

        if errors:
            return errors, HttpStatus.bad_request_400.value

        try:
            user = user_schema.load(user_dict)
            db.session.add(user)
            db.session.commit()
            query = User.query.get(user.id)
            dump_result = user_schema.dump(query)
            return dump_result, HttpStatus.created_201.value

        except SQLAlchemyError as e:
            db.session.rollback()
            response = {"error": str(e)}
            return response, HttpStatus.bad_request_400.value


routes.add_resource(UserResource, '/user/<int:id>')
