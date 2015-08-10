"""Reads in media titles and generates a webpage from the valid data"""
from movie import Movie
from tv import TvShow
import create_site
import json

# Will hold a mix of Movie and TvShow instances
media = []

# Import the individual movies and tv show titles from
# a local JSON file and create a web page from the data
with open("media.json") as json_file:
    # Read the JSON file if it is in valid format
    json_data = json.load(json_file)

    # Make sure each entry in the "movies" section of
    # the JSON file can be parsed to an instance of the
    # Movie class and likewise for the TvShows
    for movie in json_data['movies']:
        media.append(Movie(movie))
    for tv_show in json_data['tv_shows']:
        media.append(TvShow(tv_show))   

    # Generate the HTML, scripts, and stylesheets to
    # create a User-Interface from the list of Movie 
    # and TvShow objects we just assembled
    create_site.open_media_page(media)
