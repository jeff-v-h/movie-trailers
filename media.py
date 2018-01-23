import webbrowser


class Movie():
    '''This class provides a way to store movie related information.
    Attributes:
        movie_title: The movie's title.
        poster_image_url: a url link to a poster for the movie
        trailer_youtube_id: a url link to a trailer for the movie on youtube
    '''

    def __init__(self, movie_title, poster_url, youtube_trailer):
        '''This constructor method initialises a movie instance with the
        movie's title, poster url and url to the trailer from youtube '''
        self.title = movie_title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        ''' This function opens the movie's youtube trailer in a webbrowser '''
        webbrowser.open(self.trailer_youtube_url)
