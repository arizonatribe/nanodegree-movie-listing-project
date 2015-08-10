"""Defines structure of Video class."""
import webbrowser

class Video(object):
    """Base class for different visual media types."""

    def __init__(self, details):
        """Instantiates a Video instance from an object which contains expected
            members, such as 'title', 'description', and various URLs"""
        self.title = details['title']
        self.description = details['description']
        self.duration = details['duration']
        self.imdb_url = details['imdb_url']
        self.trailer_youtube_url = details['trailer_url']
        self.poster_image_url = details['pic_url']

    def show_trailer(self):
        """Opens the multimedia trailer from a site like youtube."""
        webbrowser.open(self.trailer_youtube_url)

    def get_rating(self, ratings, rating):
        """Retrieves a given rating if it exists in a provided string array of
            ratings appropriate to the particular media type."""
        if rating in ratings:
            return rating
        else:
            return ''
