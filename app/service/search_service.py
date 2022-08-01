import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel
from app.model.movie import Movie
from flask_restful import abort


def compare_data():
    data = Movie.query.all()
    movie_data_frame = pd.DataFrame([(d.title, d.overview, d.image, d.popularity, d.release_date) for d in data],
                                    columns=['title', 'overview', 'image', 'popularity', 'release_date'])
    tfv = TfidfVectorizer(min_df=1, max_features=None, strip_accents='unicode', analyzer='word',
                          token_pattern=r'\w{1,}', ngram_range=(1, 3), stop_words='english')
    tfv_matrix = tfv.fit_transform(movie_data_frame['overview'])
    sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
    indices = pd.Series(movie_data_frame.index, index=movie_data_frame['title']).drop_duplicates()
    return movie_data_frame, sig, indices


def format_results(movies):
    output = {}
    counter = 1
    for row in movies.values:
        entry = {'title': row[0], 'overview': row[1], 'image': row[2], 'popularity': row[3], 'date': str(row[4])}
        output[f"result: {counter}"] = entry
        counter += 1
    return output, 200


def get_recommendation(data):
    values = compare_data()
    index = 0
    try:
        index = values[2][data.title]
    except KeyError:
        abort(404, message="Movie searched was not found")

    sig_scores = list(enumerate(values[1][index]))
    sig_scores = sorted(sig_scores, key=lambda item: item[1], reverse=True)
    if len(sig_scores) >= 10:
        sig_scores = sig_scores[:10]

    movies_indices = [score[0] for score in sig_scores]
    return format_results(values[0].iloc[movies_indices])
