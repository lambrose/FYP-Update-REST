import unittest
from app.test import test_data
from app.utils.recommendation import get_group_recommendation
from app.utils.short_algorithms import most_pleasure


class TestMostPleasure(unittest.TestCase):

    def test_one_most_pleasure(self):
        movie = get_group_recommendation(test_data.movie_set_1, test_data.data_set_1, most_pleasure)
        self.assertEqual(movie, ['B', 'C'])

    def test_two_most_pleasure(self):
        movie = get_group_recommendation(test_data.movie_set_2, test_data.data_set_2, most_pleasure)
        self.assertEqual(movie, ["A"])

    def test_three_most_pleasure(self):
        movie = get_group_recommendation(test_data.movie_set_3, test_data.data_set_3, most_pleasure)
        self.assertEqual(movie, ["A", "B", "C"])

    def test_four_most_pleasure(self):
        movie = get_group_recommendation(test_data.movie_set_4, test_data.data_set_4, most_pleasure)
        self.assertEqual(movie, ['A'])

    def test_five_most_pleasure(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_5, most_pleasure)
        self.assertEqual(movie, ['B', 'D', 'F', 'G', 'J'])

    def test_six_most_pleasure(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_6, most_pleasure)
        self.assertEqual(movie, ['A', 'E', 'I'])

    if __name__ == '__main__':
        unittest.main()
