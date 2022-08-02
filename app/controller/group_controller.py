from flask_restful import reqparse, Resource, abort
import json

from app.service.group_recommendation_service import execute_algorithms

parser = reqparse.RequestParser()
parser.add_argument('movies', dest='movies', location='form', required=True, help='Movies are required')
parser.add_argument('ratings', dest='ratings', location='form', required=True, help='Ratings are required')


class Group(Resource):

    def post(self):
        args = parser.parse_args()
        data = json.loads(args.movies), json.loads(args.ratings)
        if len(data[0]) == len(data[1]) and len(data[0]) > 1:
            return execute_algorithms(data)
        abort(400, status="Error", message="Bad Request. Invalid data.")
