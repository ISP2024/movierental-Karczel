import csv
import logging
from typing import Optional
from movie import Movie


class MovieCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance.movies = {}
            cls._instance.load_movies()
        return cls._instance

    def load_movies(self):
        """Loads movies from a CSV file line-by-line."""
        with open('movies.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for line_number, row in enumerate(reader, start=1):
                if len(row) < 3 or row[0].startswith('#'):
                    continue

                try:
                    movie_id, title, year, *genres = row
                    year = int(year)
                    genre_list = [genre.strip() for genre in genres[0].split('|')] if genres else []
                    movie = Movie(title, year, genre_list)
                    self.movies[title] = movie
                except (ValueError, IndexError) as e:
                    logging.error(f"Line {line_number}: Unrecognized format {row}: {e}")

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """Returns a movie with a matching title and optional year."""
        if year:
            return self.movies.get(f"{title} ({year})")
        return next((movie for movie in self.movies.values() if movie.title == title), None)
