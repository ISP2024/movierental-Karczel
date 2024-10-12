import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie

class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

    def test_billing(self):
        # no rentals
        self.c.rentals = []
        self.assertEqual(self.c.total_charge(), 0.0)

        # a new release rental for 1 day
        rental1 = Rental(self.new_movie, 1)  # 1 day = 3.0
        self.c.rentals = [rental1]
        self.assertEqual(self.c.total_charge(), 3.0)

        # a regular movie rental for 2 days
        rental2 = Rental(self.regular_movie, 2)  # 2 days = 2.0
        self.c.rentals = [rental2]
        self.assertEqual(self.c.total_charge(), 2.0)

        # a children's movie rental for 4 days
        rental3 = Rental(self.childrens_movie, 4)  # 4 days = 1.5 + 1(1.5)
        self.c.rentals = [rental3]
        self.assertEqual(self.c.total_charge(), 3.0)

        # multiple rentals
        rental4 = Rental(self.new_movie, 5)  # 5 days at 3.0 per day = 15.0
        rental5 = Rental(self.regular_movie, 3)  # 3 days = 2.0 + 1(1.5) = 3.5
        rental6 = Rental(self.childrens_movie, 2)  # 2 days = 1.5

        self.c.rentals = [rental4, rental5, rental6]
        # Total charge should be 15.0 + 3.0 + 1.5 = 20.0
        self.assertEqual(self.c.total_charge(), 20.0)

        # 1-day rental for each type
        rental7 = Rental(self.new_movie, 1)  # 1 day = 3.0
        rental8 = Rental(self.regular_movie, 1)  # 1 day = 2.0
        rental9 = Rental(self.childrens_movie, 1)  # 1 day = 1.5

        self.c.rentals = [rental7, rental8, rental9]
        # Total charge should be 3.0 + 2.0 + 1.5 = 6.5
        self.assertEqual(self.c.total_charge(), 6.5)

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
