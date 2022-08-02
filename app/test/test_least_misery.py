import unittest
from app.test import test_data
from app.utils.recommendation import get_group_recommendation
from app.utils.short_algorithms import least_misery


class TestLeastMisery(unittest.TestCase):

    def test_one_least_misery(self):
        movie = get_group_recommendation(test_data.movie_set_1, test_data.data_set_1, least_misery)
        self.assertEqual(movie, ['A', 'B'])

    def test_two_least_misery(self):
        movie = get_group_recommendation(test_data.movie_set_2, test_data.data_set_2, least_misery)
        self.assertEqual(movie, ["B"])

    def test_three_least_misery(self):
        movie = get_group_recommendation(test_data.movie_set_3, test_data.data_set_3, least_misery)
        self.assertEqual(movie, ["A", "B", "C"])

    def test_four_least_misery(self):
        movie = get_group_recommendation(test_data.movie_set_4, test_data.data_set_4, least_misery)
        self.assertEqual(movie, ['B', 'D'])

    def test_five_least_misery(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_5, least_misery)
        self.assertEqual(movie, ['E', 'F'])

    def test_six_least_misery(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_6, least_misery)
        self.assertEqual(movie, ["F"])

    if __name__ == '__main__':
        unittest.main()
