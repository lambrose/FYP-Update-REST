from flask_restful import fields, reqparse, Resource
from app.service.user_service import create_user, email

parser = reqparse.RequestParser()
parser.add_argument('forename', dest='forename', location='form', required=True, help='Forename is required')
parser.add_argument('surname', dest='surname', location='form', required=True, help='Surname is required')
parser.add_argument('email', dest='email', type=email, location='form', required=True, help='Valid email is required')
parser.add_argument('password', dest='password', location='form', required=True, help='Password is required')

user_fields = {
    'forename': fields.String,
    'surname': fields.String,
    'email': fields.String,
    'password': fields.String,
}


class Register(Resource):

    def post(self):
        args = parser.parse_args()
        return create_user(args)
