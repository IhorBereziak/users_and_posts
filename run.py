from app import app

if __name__ == '__main__':
    from db import db
    from crypt import bcrypt

    db.init_app(app)
    bcrypt.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run()


