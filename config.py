class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/user_and_post'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'shjfsdljhjhjhjhjhjhjhjhgjlskhjgdf7chhjhjhlkhoohhkllllllllllllllllllllllll'

class DevConfig(Config):
    DEBUG = True