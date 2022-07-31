import datetime
import re
from flask_restful import abort
from app import db
from app.model.user import User


def create_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            forename=data.forename,
            surname=data.surname,
            email=data.email,
            password=data.password,
            register_date=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        abort(409, status="Error", message="User already exists. Please Log in")


def verify_user(data):
    user = User.query.filter_by(email=data.email).first()
    if user and user.check_password(data.password):
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 202

    abort(401, status="Error", message="Invalid user credentials")


def valid_email(email_str):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.fullmatch(regex, email_str)


def email(email_str):
    if valid_email(email_str):
        return email_str
    else:
        raise ValueError('{} is not a valid email'.format(email_str))


def save_changes(data):
    db.session.add(data)
    db.session.commit()
