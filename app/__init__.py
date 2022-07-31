from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from app.main.config import Config

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app