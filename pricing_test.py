import unittest
from datetime import datetime
from movie import Movie
from rental import Rental
from price_strategy import NewRelease, ChildrensPrice, RegularPrice

class TestRentalPriceCode(unittest.TestCase):

    def test_price_code_new_release(self):
        current_year = datetime.now().year
        movie = Movie("Oppenheimer", current_year, ["Drama", "History"])
        rental = Rental(movie, days_rented=3)

        self.assertIsInstance(rental.price_code(), NewRelease, "Price code should be NewRelease for movies released this year.")

    def test_price_code_childrens(self):
        movie = Movie("Frozen", 2013, ["Children", "Animation"])
        rental = Rental(movie, days_rented=5)

        self.assertIsInstance(rental.price_code(), ChildrensPrice, "Price code should be ChildrensPrice for children's movies.")

    def test_price_code_regular(self):
        movie = Movie("CitizenFour", 2014, ["Documentary", "Biography"])
        rental = Rental(movie, days_rented=2)

        self.assertIsInstance(rental.price_code(), RegularPrice, "Price code should be RegularPrice for regular movies.")
