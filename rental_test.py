import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from price_strategy import NewRelease, RegularPrice, ChildrensPrice


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ["Sci-Fi", "Adventure"])
        self.regular_movie = Movie("Air", 2023, ["Biography", "Drama"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Adventure", "Children"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ["Biography", "Drama"])
        self.assertEqual("Air", m.title)
        self.assertEqual(2023, m.year)
        self.assertEqual(["Biography", "Drama"], m.genre)
        self.assertTrue(m.is_genre("Biography"))
        self.assertTrue(m.is_genre("Drama"))

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1, NewRelease())
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5, NewRelease())
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 1, RegularPrice())
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 5, RegularPrice())
        self.assertEqual(rental.get_price(), 6.5)
        rental = Rental(self.childrens_movie, 1, ChildrensPrice())
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5, ChildrensPrice())
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 3, NewRelease())
        self.assertEqual(rental.get_rental_points(), 3)
        rental = Rental(self.regular_movie, 5, RegularPrice())
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 4, ChildrensPrice())
        self.assertEqual(rental.get_rental_points(), 1)
