import requests
from app import db
from app.model.movie import Movie


url = "https://api.tmdb.org/3/discover/movie/?api_key=<API-KEY>"
movie_keys = {'title', 'overview', 'poster_path', 'genre_ids', 'popularity', 'release_date'}
genres = {28: False, 12: False, 16: False, 35: False, 80: False, 99: False, 18: False, 10751: False, 14: False,
          36: False, 27: False, 10402: False, 9648: False, 10749: False, 878: False, 10770: False, 53: False,
          10752: False, 37: False}


def truncate_table():
    db.engine.execution_options(autocommit=True).execute("TRUNCATE TABLE movie")


def insert_movies():
    truncate_table()
    genre_ids = genres
    for page in range(1, 50):
        req = requests.get(url=url, params={'page': page})
        for movie in req.json()["results"]:
            if movie_keys.issubset(movie.keys()):
                for genre_id in movie.get('genre_ids'):
                    genre_ids[genre_id] = True
                    save_to_db(movie, genre_ids)


def save_to_db(movie, genre_ids):
    stored_movie = Movie.query.filter_by(title=movie['title'], overview=movie['overview']).first()
    if not stored_movie:
        entry = Movie(title=movie['title'], overview=movie['overview'], image=movie['poster_path'],
                      action=genre_ids[28], adventure=genre_ids[12], animation=genre_ids[16], comedy=genre_ids[35],
                      crime=genre_ids[80], documentary=genre_ids[99], drama=genre_ids[18], family=genre_ids[10751],
                      fantasy=genre_ids[14], history=genre_ids[36], horror=genre_ids[27], musical=genre_ids[10402],
                      mystery=genre_ids[9648], romance=genre_ids[10749], sci_fi=genre_ids[878],
                      tv_movie=genre_ids[10770], thriller=genre_ids[53], war=genre_ids[10752], western=genre_ids[37],
                      popularity=movie['popularity'], release_date=movie['release_date'])
        try:
            db.session.add(entry)
            db.session.commit()
            genre_ids = genres
        except Exception:
            print(movie)
