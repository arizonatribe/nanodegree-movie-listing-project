"""Defines structure of Movie class."""
from video import Video

class Movie(Video):
    """ This class provides a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, details):
        """Creates a new instance of a Movie. Should be provided with media
            details in a given object, including some values specific to Movies."""
        Video.__init__(self, details)
        self.year = details['year']
        self.rating = Video.get_rating(self, Movie.VALID_RATINGS, details['rating'])
