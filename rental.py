import logging

from movie import Movie
from datetime import datetime
from price_strategy import PriceStrategy, NewRelease, RegularPrice, ChildrensPrice


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
    	   a movie with known rental period (daysRented).
    	"""
        self.movie = movie
        self.days_rented = days_rented

    def movie(self):
        return self.movie

    def days_rented(self):
        return self.days_rented

    def get_price(self):
        """Compute rental charge by delegating to the movie's price strategy."""
        return self.price_code().get_price(self.days_rented)

    def get_rental_points(self):
        return self.price_code().get_rental_points(self.days_rented)

    def price_code(self) -> PriceStrategy:
        current_year = datetime.now().year
        if self.movie.year == current_year:
            return NewRelease()
        elif "Children" in self.movie.genre:
            return ChildrensPrice()
        else:
            return RegularPrice()
