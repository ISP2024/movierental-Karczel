from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Base class for price strategies."""

    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days):
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days):
        """The frequent renter points earned for this rental."""
        pass

class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_price(self, days):
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days):
        return 1


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children's movies."""

    def get_price(self, days):
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days):
        return 1


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_price(self, days):
        return 3.0 * days

    def get_rental_points(self, days):
        return days  # 1 point for each day rented
