from rental import Rental


class Customer:
    """A customer who rents movies.

    The customer object holds information about the
    movies rented for the current billing period,
    and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        """Add a rental for this customer"""
        if rental not in self.rentals:
            self.rentals.append(rental)
    
    def get_name(self):
        """Get the customer's name."""
        return self.name
    
    def statement(self):
        """Create a statement of rentals for the current period.

        Print all the rentals in the current period, 
        along with total charges and frequent renter points.
        
        Returns:
            the statement as a String
        """

        # Generate the header section of the statement
        statement = self.header()

        rental_fmt = "{:40s}  {:6d} {:6.2f}\n"
        details = ""
        # Generate the rental details
        statement += self.rental_details(rental_fmt, details)

        # Generate the footer section (total charges and frequent renter points)
        statement += self.footer()

        return statement

    def header(self):
        header_fmt = "{:40s}  {:6s} {:6s}\n"
        return f"Rental Report for {self.name}\n\n" + header_fmt.format("Movie Title", "  Days", " Price")

    def rental_details(self, rental_fmt, details, index=0):
        if index >= len(self.rentals):
            return ""
        rental = self.rentals[index]

        # Handle edge case: if rental days are negative
        if rental.get_days_rented() < 0:
            raise ValueError(f"Rental days cannot be negative for movie: {rental.get_movie().get_title()}")

        # Add details to the statement
        details += rental_fmt.format(
            rental.get_movie().get_title(),
            rental.get_days_rented(),
            rental.get_price()
        )
        return details

    def footer(self):
        footer = "\n"
        footer += "{:40s}  {:6s} {:6.2f}\n".format("Total Charges", "", self.total_charge())
        footer += "Frequent Renter Points earned: {}\n".format(self.get_total_rental_points())
        return footer

    def get_total_rental_points(self,index=0):
        """Calculate the total rental charges for the current rentals."""
        if index >= len(self.rentals):
            return 0
        return self.rentals[index].rental_points() + self.total_charge(index+1)

    def total_charge(self,index=0):
        """Calculate the total rental charges for the current rentals."""
        if index >= len(self.rentals):
            return 0
        return self.rentals[index].get_price() + self.total_charge(index+1)