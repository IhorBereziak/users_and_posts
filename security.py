from app.models.user import UserModel
from crypt import bcrypt


def auth(email, password):
    user = UserModel.get_by_email(email)
    if user and bcrypt.check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    user = UserModel.get_by_id(user_id)
    if user:
        return user
