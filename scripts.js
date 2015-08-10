(function() {
    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });
    // Start playing the video whenever the trailer modal is opened
    $(document).on('click', '.movie-tv-tile', function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id'),
            sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1',
            imdbUrl = $(this).attr('data-imdb-url'),
            synopsis = $(this).attr('data-synopsis'),
            yearMade = $(this).attr('data-year-made'),
            networkUrl = $(this).attr('data-network-url'),
            duration = $(this).attr('data-duration') + ' mins',
            mediaTitle = $(this).find('h2.media-title').text(),
            modalMediaTitle = mediaTitle + (yearMade ? ' (' + yearMade + ')' : '');
    
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
          'id': 'trailer-video',
          'type': 'text-html',
          'src': sourceUrl,
          'frameborder': 0
        }));
        $('.modal-header')
          .empty()
          .append($("<h2></h2>").text(modalMediaTitle));
            
        $('#video-info-container')
            .empty()
            .append($("<p></p>")
              .attr('class', 'p-synopsis')
              .text(synopsis)
            )
            .append($("<h3></h3>")
              .attr('class', 'h-duration')
              .text(duration)
            )
            .append($("<a></a>", {
                href: imdbUrl,
                'class': 'logo-icon',
                target: '_blank'
              })
              .append($('<img />', {
                  src: 'https://upload.wikimedia.org/wikipedia/commons/3/35/IMDb_logo.svg',
                  height: 35,
                  alt: 'Television network link'
                })
              )
            );
        
        if (networkUrl) {
          $('#video-info-container')
            .append($('<img />', {
                src: networkUrl,
                height: 35,
                alt: 'Television network link'
              })
            );
        }
    
    });
    // Animate in the movies when the page loads
    $(document).ready(function () {
      $('.media-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
      });
    });    
})();