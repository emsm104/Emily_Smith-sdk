import unittest
import os
import sys
from movies import (
    Movie,
    get_all_movies,
    get_movie_by_id,
    get_movie_by_name,
    get_sorted_movies,
    get_movie_by_regex
)


class TestMovies(unittest.TestCase):
    """
    Testing suite for movies.py.
    """
    def test_movie_class(self):
        """
        Test the creation of a Movie class.
        """
        movie = Movie()
        self.assertEqual(movie.id,"")
        self.assertEqual(movie.name,"")
        self.assertEqual(movie.runtimeInMinutes,0)
        self.assertEqual(movie.budgetInMillions,0)
        self.assertEqual(movie.boxOfficeRevenueInMillions,0)
        self.assertEqual(movie.academyAwardNominations,0)
        self.assertEqual(movie.academyAwardWins,0)
        self.assertEqual(movie.rottenTomatoesScore,0)

    def test_get_all_movies(self):
        """
        Test get_all_movies().
        """
        test_movies = get_all_movies()
        self.assertEqual(len(test_movies), 8)

    def test_get_movie_by_id(self):
        """
        Test get_movie_by_id().
        """
        movie_by_id = get_movie_by_id("5cd95395de30eff6ebccde56")
        self.assertEqual(movie_by_id.id, "5cd95395de30eff6ebccde56")
        self.assertEqual(movie_by_id.name, "The Lord of the Rings Series")
        self.assertEqual(movie_by_id.runtimeInMinutes, 558)
        self.assertEqual(movie_by_id.budgetInMillions, 281)
        self.assertEqual(movie_by_id.boxOfficeRevenueInMillions, 2917)
        self.assertEqual(movie_by_id.academyAwardNominations, 30)
        self.assertEqual(movie_by_id.academyAwardWins, 17)
        self.assertEqual(movie_by_id.rottenTomatoesScore, 94)

    def test_get_movie_by_name(self):
        """
        Test get_movie_by_name().
        """
        movie_by_name = get_movie_by_name("The Lord of the Rings Series")
        self.assertEqual(movie_by_name.id, "5cd95395de30eff6ebccde56")
        self.assertEqual(movie_by_name.name, "The Lord of the Rings Series")
        self.assertEqual(movie_by_name.runtimeInMinutes, 558)
        self.assertEqual(movie_by_name.budgetInMillions, 281)
        self.assertEqual(movie_by_name.boxOfficeRevenueInMillions, 2917)
        self.assertEqual(movie_by_name.academyAwardNominations, 30)
        self.assertEqual(movie_by_name.academyAwardWins, 17)
        self.assertEqual(movie_by_name.rottenTomatoesScore, 94)
    
    def test_get_sorted_movies_asc(self):
        """
        Test get_sorted_movies().
        """
        test_asc_movies = get_sorted_movies("_id","asc")
        self.assertEqual(test_asc_movies[0].id, "5cd95395de30eff6ebccde56")
        self.assertEqual(test_asc_movies[0].name, "The Lord of the Rings Series")
        self.assertEqual(test_asc_movies[0].runtimeInMinutes, 558)
        self.assertEqual(test_asc_movies[0].budgetInMillions, 281)
        self.assertEqual(test_asc_movies[0].boxOfficeRevenueInMillions, 2917)
        self.assertEqual(test_asc_movies[0].academyAwardNominations, 30)
        self.assertEqual(test_asc_movies[0].academyAwardWins, 17)
        self.assertEqual(test_asc_movies[0].rottenTomatoesScore, 94)

    def test_get_sorted_movies_desc(self):
        """
        Test get_sorted_movies().
        """
        test_asc_movies = get_sorted_movies("_id","desc")
        self.assertEqual(test_asc_movies[0].id, "5cd95395de30eff6ebccde5d")
        self.assertEqual(test_asc_movies[0].name, "The Return of the King")
        self.assertEqual(test_asc_movies[0].runtimeInMinutes, 201)
        self.assertEqual(test_asc_movies[0].budgetInMillions, 94)
        self.assertEqual(test_asc_movies[0].boxOfficeRevenueInMillions, 1120)
        self.assertEqual(test_asc_movies[0].academyAwardNominations, 11)
        self.assertEqual(test_asc_movies[0].academyAwardWins, 11)
        self.assertEqual(test_asc_movies[0].rottenTomatoesScore, 95)

    def test_get_movies_by_regex(self):
        """
        Test get_movies_by_regex(). 
        """
        test_books = get_movie_by_regex("name", "/King/i")
        self.assertIn("King",test_books[0].name)


if __name__ == "__main__":
    unittest.main()