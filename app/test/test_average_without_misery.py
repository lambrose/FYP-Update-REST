import unittest
from app.test import test_data
from app.utils.recommendation import get_group_recommendation
from app.utils.short_algorithms import average_without_misery


class TestAverageWithoutMisery(unittest.TestCase):

    def test_one_average_without_misery(self):
        movie = get_group_recommendation(test_data.movie_set_1, test_data.data_set_1, average_without_misery)
        self.assertEqual(movie, ['B'])

    def test_two_average_without_misery(self):
        movie = get_group_recommendation(test_data.movie_set_2, test_data.data_set_2, average_without_misery)
        self.assertEqual(movie, ["B"])

    def test_three_average_without_misery(self):
        movie = get_group_recommendation(test_data.movie_set_3, test_data.data_set_3, average_without_misery)
        self.assertEqual(movie, ["A", "B", "C"])

    def test_four_average_without_misery(self):
        movie = get_group_recommendation(test_data.movie_set_4, test_data.data_set_4, average_without_misery)
        self.assertEqual(movie, ["A", "B", "C", "D"])

    def test_five_average_without_misery(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_5, average_without_misery)
        self.assertEqual(movie, ['F'])

    def test_six_average_without_misery(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_6, average_without_misery)
        self.assertEqual(movie, ['E', 'F'])

    if __name__ == '__main__':
        unittest.main()
