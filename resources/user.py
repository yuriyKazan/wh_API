from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='The field can\'t be empty')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='The field can\'t be empty')

    @jwt_required()
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'A user with username already exist'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User created successfully'}, 201
