from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.config import Config


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name=Config):
    app = Flask(__name__)
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    from app.controller.register_controller import Register
    from app.controller.login_controller import Login

    app.config.from_object(Config)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')
    app.register_blueprint(api_bp)

    return app
