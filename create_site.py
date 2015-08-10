"""Generates HTML and links in the necessary scripts and styles for the page."""
import webbrowser
import os
import re
from movie import Movie
from tv import TvShow
from shutil import copyfile

# markup for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Some Favorite Movies and TV Shows!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="https://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="styles.css">
    <script type="text/javascript" charset="utf-8" src="scripts.js"></script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal fade" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="modal-header bg-primary">
          </div>
          <div class="modal-body">
            <div class="scale-media" id="trailer-video-container">
            </div>
            <div class="scale-media" id="video-info-container">
            </div>   
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Some Favorite Movies and TV Shows</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <ul class="nav nav-tabs">
        <li class="active"><a data-toggle="tab" href="#movie-pane">Movies</a></li>
        <li><a data-toggle="tab" href="#tv-show-pane">TV Shows</a></li>
      </ul>
      <div class="tab-content">
        <div id="movie-pane" class="tab-pane fade in active">
          {movie_tiles}
        </div>
        <div id="tv-show-pane" class="tab-pane fade">
          {tv_tiles}
        </div>
      </div>
    </div>
  </body>
</html>
'''

# A single movie template. Each valid Movie has its members interpolated against
# the properties named in this template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tv-tile text-center" data-duration="{duration}" data-year-made="{year_made}" data-synopsis="{media_description}" data-trailer-youtube-id="{trailer_youtube_id}" data-imdb-url="{imdb_url}" data-toggle="modal" data-target="#trailer">
  <img src="{poster_image_url}" width="220" height="342">
  <h2 class="media-title">{media_title}</h2>
</div>
'''

# A single TV template. Each valid TvShow has its members interpolated against
# the properties named in this template
tv_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tv-tile text-center" data-duration="{duration}" data-network-url="{network_url}" data-synopsis="{media_description}" data-trailer-youtube-id="{trailer_youtube_id}" data-imdb-url="{imdb_url}" data-toggle="modal" data-target="#trailer">
  <img src="{poster_image_url}" width="300" height="169">
  <h2 class="media-title">{media_title}</h2>
</div>
'''

def create_tiles_content(media):
    """Iterates through a collection of media titles and generates HTML markup
      from each valid title."""

    movie_content = ''
    tv_content = ''
    # The HTML content for this section of the page
    for item in media:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', item.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', item.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie/tv-show with its content filled in
        if isinstance(item, Movie):
            movie_content += movie_tile_content.format(
                media_title=item.title,
                poster_image_url=item.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                imdb_url=item.imdb_url,
                media_description=item.description,
                year_made=item.year,
                duration=item.duration
            )
        elif isinstance(item, TvShow):
            tv_content += tv_tile_content.format(
                media_title=item.title,
                poster_image_url=item.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                imdb_url=item.imdb_url,
                media_description=item.description,
                network_url=item.network_url,
                duration=item.duration
            )

    return main_page_content.format(movie_tiles=movie_content, tv_tiles=tv_content)

def open_media_page(media):
    """Creates and (optionally) opens an HTML file. Also copies styles and scripts"""

    # Create or overwrite the output file
    output_html = open('./public/index.html', 'w')

    # Replace the placeholder for the media tiles with the actual dynamically generated content
    rendered_content = create_tiles_content(media)

    # Output the files
    output_html.write(main_page_head + rendered_content)
    output_html.close()

    # copy the scripts and stylesheets to the public, distributable directory
    copyfile('scripts.js', './public/scripts.js')
    copyfile('styles.css', './public/styles.css')

    # open the output html file in the browser
    url = os.path.abspath(output_html.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
