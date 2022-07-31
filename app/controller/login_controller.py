from flask_restful import fields, reqparse, Resource
from app.service.user_service import verify_user, email

parser = reqparse.RequestParser()
parser.add_argument('email', dest='email', type=email, location='form', required=True, help='valid email is required')
parser.add_argument('password', dest='password', location='form', required=True, help='password is required')

user_fields = {
    'email': fields.String,
    'password': fields.String,
}


class Login(Resource):

    def post(self):
        args = parser.parse_args()
        return verify_user(args)
