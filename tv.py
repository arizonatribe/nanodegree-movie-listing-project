"""Defines structure of TV Show class."""
from video import Video

class TvShow(Video):
    """Holds and provides information on a Television show."""
    
    VALID_RATINGS = ["TV-Y", "TV-Y7", "TV-G", "TV-PG", "TV-14", "TV-MA"]
    
    def __init__(self, details):
        """Creates a new instance of a TvShow. Should be provided with media
            details in a given object, including some values specific to TV."""
        Video.__init__(self, details)
        self.seasons = details['seasons']
        self.network_url = details['network_url']
        self.rating = Video.get_rating(self, TvShow.VALID_RATINGS, details['rating'])
