def plurality_voting(movies, users_ratings):
    users_preferences = {}
    max_occurrence = 0
    recommendation = []
    for ratings in users_ratings:
        max_user_rating = max(ratings)
        for index, rating in enumerate(ratings):
            if rating == max_user_rating:
                users_preferences[movies[index]] = 1 + users_preferences.get(movies[index], 0)
                max_occurrence = max(users_preferences[movies[index]], max_occurrence)

    for movie, occurrence in users_preferences.items():
        if max_occurrence == occurrence:
            recommendation.append(movie)

    return recommendation


def borda_count(users_ratings) -> list:
    new_user_ratings = []
    for ratings in users_ratings:
        ratings = sorted(enumerate(ratings), key=lambda x: x[1])
        new_ratings = [0.0] * len(ratings)
        res = {}
        for index, rating in ratings:
            if res.get(rating):
                res[rating].append(index)
            else:
                res[rating] = [index]

        for index, key in enumerate(res.keys()):
            for val in res[key]:
                new_ratings[val] = index + (1/len(res[key]))
        new_user_ratings.append(new_ratings)
    return new_user_ratings
