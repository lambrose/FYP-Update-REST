from flask_restful import fields, reqparse, Resource
from app.service.user_service import create_user, email

parser = reqparse.RequestParser()
parser.add_argument('forename', dest='forename', location='form', required=True, help='forename is required')
parser.add_argument('surname', dest='surname', location='form', required=True, help='surname is required')
parser.add_argument('email', dest='email', type=email, location='form', required=True, help='valid email is required')
parser.add_argument('password', dest='password', location='form', required=True, help='password is required')

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
