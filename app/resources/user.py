from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt import jwt_required

from app.models.post import PostModel
from app.models.user import UserModel
from app.schemas.post import PostSchema
from app.schemas.user import UserSchema, UserUpdateSchema
from crypt import bcrypt


class User(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        error = UserSchema().validate(data)
        if error:
            return {'message': error}, 400
        user = UserModel(**data)
        if UserModel.get_by_email(user.email):
            return {'message': f'User with email {user.email} already exist'}, 400
        user.password = bcrypt.generate_password_hash(user.password, 10)
        user.save()
        return {'message': 'User was created'}, 201

    @classmethod
    def get(cls, user_id):
        user = UserModel.get_by_id(user_id)
        if not user:
            return {'massage': 'user not found'}, 404
        return UserSchema().dump(user)

    @classmethod
    def put(cls, user_id):
        data = request.get_json()
        create_error = UserSchema().validate(data)
        update_error = UserUpdateSchema().validate(data)
        if update_error:
            return {'message': update_error}, 400
        if data.get('password', None):
            data['password'] = bcrypt.generate_password_hash(data['password'], 10)
        user_by_id = UserModel.get_by_id(user_id)
        if user_by_id:
            try:
                UserModel.update_by_id(user_id, data)
                return {'message': 'user was updated'}, 200
            except IntegrityError as err:
                return {'message': err.args}, 400
        if create_error:
            return {'message': create_error}, 400
        user = UserModel(**data)
        if UserModel.get_by_email(user.email):
            return {'message': f'User with email {user.email} already exist'}, 400
        user.password = bcrypt.generate_password_hash(user.password)
        user.save()
        return {'message': 'User was created'}, 201

    @classmethod
    def delete(cls, user_id):
        result = UserModel.del_by_id(user_id)
        if not result:
            return {'message': 'User is not found'}, 400
        return {'message': 'User was deleted'}, 200

class UserAddPost(Resource):
    @classmethod
    def post(cls, user_id):
        data = request.get_json()
        error = PostSchema().validate(data)
        if error:
            return {'message': error}, 400
        user = UserModel.get_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        user.posts.append(PostModel(**data))
        user.save()
        return {'message': 'Post was added to user'}, 201

class UserAll(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        users = UserModel.get_all()
        return {'user': UserSchema(many=True).dump(users)}
