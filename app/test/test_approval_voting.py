import unittest
from app.test import test_data
from app.utils.recommendation import get_group_recommendation
from app.utils.short_algorithms import approval_voting


class TestApprovalVoting(unittest.TestCase):

    def test_one(self):
        movie = get_group_recommendation(test_data.movie_set_1, test_data.data_set_1, approval_voting)
        self.assertEqual(movie, ['A', 'B', 'C'])

    def test_two(self):
        movie = get_group_recommendation(test_data.movie_set_2, test_data.data_set_2, approval_voting)
        self.assertEqual(movie, ["A"])

    def test_three(self):
        movie = get_group_recommendation(test_data.movie_set_3, test_data.data_set_3, approval_voting)
        self.assertEqual(movie, ["A", "B", "C"])

    def test_four(self):
        movie = get_group_recommendation(test_data.movie_set_4, test_data.data_set_4, approval_voting)
        self.assertEqual(movie, ['A', 'B', 'C', 'D'])

    def test_five(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_5, approval_voting)
        self.assertEqual(movie, ['C', 'D', 'E', 'F', "J"])

    def test_six(self):
        movie = get_group_recommendation(test_data.movie_set_5_6, test_data.data_set_6, approval_voting)
        self.assertEqual(movie, ["D", "E", "F", "H", "J"])

    if __name__ == '__main__':
        unittest.main()
