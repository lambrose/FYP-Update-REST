def get_group_recommendation(movies: list, ratings: list, function) -> list:
    max_value = 0
    recommendation = []
    index = 0

    for rating in zip(*ratings):
        value = function(rating)
        if value > max_value:
            max_value = value
            recommendation = [movies[index]]
        elif value == max_value:
            recommendation.append(movies[index])
        index += 1
    return recommendation
