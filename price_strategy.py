class PriceStrategy:
    """Base class for price strategies."""

    def get_price(self, days):
        raise NotImplementedError

    def get_rental_points(self, days):
        raise NotImplementedError


class RegularPriceStrategy(PriceStrategy):
    def get_price(self, days):
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days):
        return 1


class ChildrensPriceStrategy(PriceStrategy):
    def get_price(self, days):
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days):
        return 1


class NewReleasePriceStrategy(PriceStrategy):
    def get_price(self, days):
        return 3.0 * days

    def get_rental_points(self, days):
        return days  # 1 point for each day rented
