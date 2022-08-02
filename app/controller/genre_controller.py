from flask_restful import reqparse, Resource
from app.service.movie_service import get_movies_by_genre

parser = reqparse.RequestParser()
parser.add_argument('genre', dest='genre', location='form', required=True, help='Movie genre is required')


class Genre(Resource):

    def post(self):
        args = parser.parse_args()
        return get_movies_by_genre(args)
