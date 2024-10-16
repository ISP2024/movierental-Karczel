class Movie:
    """
    A movie available for rent.
    """
    
    def __init__(self, title, price_strategy):
        # Initialize a new movie. 
        self.title = title
        self.price_strategy = price_strategy

    def get_price_strategy(self):
        return self.price_strategy

    def get_price(self, days):
        return self.price_strategy.get_price(days)

    def get_rental_points(self, days):
        return self.price_strategy.get_rental_points(days)
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title
