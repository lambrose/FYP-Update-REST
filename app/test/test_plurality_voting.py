import unittest
from app.test import test_data
from app.utils.long_algorithms import plurality_voting


class TestPluralityVoting(unittest.TestCase):

    def test_one(self):
        movie = plurality_voting(test_data.movie_set_1, test_data.data_set_1)
        self.assertEqual(movie, ["B"])

    def test_two(self):
        movie = plurality_voting(test_data.movie_set_2, test_data.data_set_2)
        self.assertEqual(movie, ['B', 'A'])

    def test_three(self):
        movie = plurality_voting(test_data.movie_set_3, test_data.data_set_3)
        self.assertEqual(movie, ["A", "B", "C"])

    def test_four(self):
        movie = plurality_voting(test_data.movie_set_4, test_data.data_set_4)
        self.assertEqual(movie, ["A"])

    def test_five(self):
        movie = plurality_voting(test_data.movie_set_5_6, test_data.data_set_5)
        self.assertEqual(movie, ['B', 'F'])

    def test_six(self):
        movie = plurality_voting(test_data.movie_set_5_6, test_data.data_set_6)
        self.assertEqual(movie, ["A"])

    def test_seven(self):
        movie = plurality_voting(test_data.movie_set_7, test_data.data_set_7)
        self.assertEqual(movie, ['C', 'A', 'B'])

    if __name__ == '__main__':
        unittest.main()
