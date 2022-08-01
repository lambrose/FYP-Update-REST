from flask_restful import Resource
from app.service.movie_service import get_movies


class Watch(Resource):

    def get(self):
        return get_movies()
