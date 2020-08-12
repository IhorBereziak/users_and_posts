from flask import request
from flask_restful import Resource

from app.models.post import PostModel
from app.schemas.post import PostSchema


class Post(Resource):
    @classmethod
    def get(cls):
        user_id = request.args.get('user_id', None)
        if user_id:
            posts = PostModel.get_by_user_id(user_id)
            return {'posts': PostSchema(many=True).dump(posts)}, 200
        posts = PostModel.get_all()
        return {'posts': [PostSchema().dump(post) for post in posts]}, 200

class PostById(Resource):
    @classmethod
    def get(cls, post_id):
        post = PostModel.get_by_id(post_id)
        if not post:
            return {'message': 'post not found'}, 400
        return PostSchema().dump(post), 200
