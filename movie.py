from dataclasses import dataclass
from collections.abc import Collection

@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genre: Collection[str]

    def __str__(self): 
        return f"{self.title}({self.year})"

    def is_genre(self, string: str) -> bool:
        return string.lower() in [g.lower() for g in self.genre]
