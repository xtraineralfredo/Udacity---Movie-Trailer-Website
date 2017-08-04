import webbrowser


class Movie():
        """This class creates instances of a movie object that contains
        information pertaining to the movie including it's title, storyline
        poster image, and a movie trailer for the user to watch when they
        click on the image of the poster."""

        def __init__(self, movie_title, movie_storyline, poster_image,
                     trailer_youtube):
                """The inputs here contain four attributes referencing to
                the movie object including the title, storyline, poster, and
                trailer. The __init__ function allows for multiple movie
                objects to be created."""
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

        # This function calls for a method to access the movie object and
        # be opened through the users browser.
        def show_trailer(self):
            """
            Intitializing instance for opening the youtube video
            """
            webbrowser.open(self.trailer_youtube_url)
