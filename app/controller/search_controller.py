from flask_restful import fields, reqparse, Resource

from app.service.search_service import get_recommendation

parser = reqparse.RequestParser()
parser.add_argument('title', dest='title', location='form', required=True, help='Movie title is required')

search_fields = {
    'title': fields.String
}


class Search(Resource):

    def post(self):
        args = parser.parse_args()
        return get_recommendation(args)
