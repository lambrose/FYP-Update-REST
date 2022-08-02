import unittest
from app.service.group_recommendation_service import execute_algorithms
from app.test.test_data import algo_data_1, algo_data_2


class TestGroupRecommendationService(unittest.TestCase):

    def test_one(self):
        expected = {'multiplicative_utilitarian': 2, 'additive_utilitarian': 2, 'approval_voting': 2, 'least_misery': 2,
                    'most_pleasure': 0, 'average_without_misery': 2, 'plurality_voting': 1, 'borda_count': 2,
                    'winner': ['C']}

        actual = execute_algorithms(algo_data_1)
        self.assertEqual(expected, actual[0])

    def test_two(self):
        expected = {'multiplicative_utilitarian': 2, 'additive_utilitarian': 2, 'approval_voting': 2, 'least_misery': 2,
                    'most_pleasure': 1, 'average_without_misery': 2, 'plurality_voting': 2, 'borda_count': 2,
                    'winner': ['D']}

        actual = execute_algorithms(algo_data_2)
        self.assertEqual(expected, actual[0])

    if __name__ == '__main__':
        unittest.main()
