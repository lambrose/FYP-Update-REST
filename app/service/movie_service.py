from app.model.movie import Movie
from flask_restful import abort


def format_results(movies):
    output = {}
    counter = 1
    for movie in movies:
        entry = {'title': movie.title, 'overview': movie.overview, 'image': movie.image, 'popularity': movie.popularity, 'date': str(movie.release_date)}
        output[f"result: {counter}"] = entry
        counter += 1
    return output, 200


def get_movies():
    movies = Movie.query.all()
    if movies:
        return format_results(movies)
    abort(500, message="Internal server error")


def get_movies_by_genre(data):
    if hasattr(Movie, data.genre):
        movies = Movie.query.filter(getattr(Movie, data.genre)).all()
        return format_results(movies)
    abort(404, message="Genre selected was not found")
