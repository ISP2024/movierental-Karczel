from collections.abc import Collection

class Movie:
    """
    A movie available for rent.
    """
    
    def __init__(self, title: str, year: int, genre: Collection[str]):
        # Initialize a new movie. 
        self.__title = title
        self.__year = year
        self.__genre = genre

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @property
    def genre(self):
        return self.__genre

    def is_genre(self, string):
        return string in self.genre
    
    def __str__(self):
        return f"{self.title}({self.year})"
