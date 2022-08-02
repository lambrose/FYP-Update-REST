import unittest
from app.test import test_data
from app.utils.recommendation import get_group_recommendation
from app.utils.short_algorithms import multiplicative_utilitarian


class TestMultiplicativeUtilitarian(unittest.TestCase):

    def test_one(self):
        movie = get_group_recommendation(test_data.movie_set_1, test_data.data_set_1, multiplicative_utilitarian)
        self.assertEqual(movie, ["B"])

    def test_two(self):
        movie = get_group_recommendation(test_data.movie_set_2, test_data.data_set_2, multiplicative_utilitarian)
        self.assertEqual(movie, ["B"])

    def test_three(self):
        movie = get_group_recommendation(test_data.movie_set_3, test_data.data_set_3, multiplicative_utilitarian)
        self.assertEqual(movie, ["A", "B", "C"])

    def test_four(self):
        movie = get_group_recommendation(test_data.movie_set_4, test_data.data_set_4, multiplicative_utilitarian)
        self.assertEqual(movie, ["B"])

    def test_five(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_5, multiplicative_utilitarian)
        self.assertEqual(movie, ["F"])

    def test_six(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_6, multiplicative_utilitarian)
        self.assertEqual(movie, ["F"])

    if __name__ == '__main__':
        unittest.main()
