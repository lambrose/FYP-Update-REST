import unittest
from app.test import test_data
from app.utils.long_algorithms import borda_count
from app.utils.recommendation import get_group_recommendation
from app.utils.short_algorithms import additive_utilitarian


class TestBordaCount(unittest.TestCase):

    def test_one(self):
        movie = get_group_recommendation(test_data.movie_set_1, borda_count(test_data.data_set_1), additive_utilitarian)
        self.assertEqual(movie, ["B"])

    def test_two(self):
        movie = get_group_recommendation(test_data.movie_set_1, borda_count(test_data.data_set_2), additive_utilitarian)
        self.assertEqual(movie, ["A", "B"])

    def test_three(self):
        movie = get_group_recommendation(test_data.movie_set_1, borda_count(test_data.data_set_3), additive_utilitarian)
        self.assertEqual(movie, ["A", "B", "C"])

    def test_four(self):
        movie = get_group_recommendation(test_data.movie_set_1, borda_count(test_data.data_set_4), additive_utilitarian)
        self.assertEqual(movie, ["A"])

    def test_five(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, borda_count(test_data.data_set_5), additive_utilitarian)
        self.assertEqual(movie, ["F"])

    def test_six(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, borda_count(test_data.data_set_6), additive_utilitarian)
        self.assertEqual(movie, ["E"])

    if __name__ == '__main__':
        unittest.main()
