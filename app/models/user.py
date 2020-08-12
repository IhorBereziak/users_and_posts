from db import db
from .post import PostModel


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    posts = db.relationship(PostModel, backref='user', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def query_filter_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id)

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query_filter_by_id(user_id).first()

    @classmethod
    def update_by_id(cls, user_id, data):
        cls.query_filter_by_id(user_id).update(data)
        db.session.commit()

    @classmethod
    def del_by_id(cls, user_id):
        result = cls.query_filter_by_id(user_id).delete()
        if result:
            db.session.commit()
        return result

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()