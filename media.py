import webbrowser

#Create a movie class
class Movie():
    """ This class defines movie information """

    #Class variable that stores valid rating in case it's needed
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #Constructor method for create instances
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Class method to open a webbrowser window with the youtube trailer url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
