from app import db
from app.model.group import Group
from app.utils.long_algorithms import plurality_voting, borda_count
from app.utils.recommendation import get_group_recommendation
from app.utils.short_algorithms import multiplicative_utilitarian, additive_utilitarian, approval_voting, \
    least_misery, most_pleasure, average_without_misery


def populate_record(record, algos, results, algorithm):
    algos[str(algorithm.__name__)] = results
    for result in results:
        record[result] = 1 + record.get(result, 0)


def get_winner(record):
    res = {}
    max_result = 0
    for movie, result in record.items():
        max_result = max(max_result, result)
        res[result] = [movie] if result not in res.keys() else res[result] + [movie]
    return res[max_result]


def format_algorithm_results(algos, winner):
    for algorithm, movie in algos.items():
        if movie == winner:
            algos[algorithm] = 2
        elif set(movie).intersection(set(winner)):
            algos[algorithm] = 1
        else:
            algos[algorithm] = 0
    algos['winner'] = winner


def execute_algorithms(data):
    movies, ratings = data
    algos = {}
    record = {}
    algorithms = [multiplicative_utilitarian, additive_utilitarian, approval_voting, least_misery, most_pleasure,
                  average_without_misery]

    for algorithm in algorithms:
        populate_record(record, algos, get_group_recommendation(movies, ratings, algorithm), algorithm)

    populate_record(record, algos, plurality_voting(movies, ratings), plurality_voting)
    populate_record(record, algos, get_group_recommendation(movies, borda_count(ratings), additive_utilitarian), borda_count)

    format_algorithm_results(algos, get_winner(record))

    # save_result(algos)

    return algos, 200


def save_result(data):
    for winner in data['winner']:
        group = Group(winner=winner, multiplicative_utilitarian=data['multiplicative_utilitarian'],
                      additive_utilitarian=data['additive_utilitarian'], approval_voting=data['approval_voting'],
                      least_misery=data['least_misery'], most_pleasure=data['most_pleasure'],
                      average_without_misery=data['average_without_misery'], plurality_voting=data['plurality_voting'],
                      borda_count=data['borda_count'])
        db.session.add(group)
        db.session.commit()
