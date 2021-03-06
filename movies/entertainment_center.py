import fresh_tomatoes
import media

doctor_strange = media.Movie(
    "Doctor Strange",
    "A story of a an arrogant doctor who turns into a"
    "magic wielding super hero",
    "http://static.srcdn.com/wp-content/uploads/Docto"
    "r-Strange-Poster.jpg",
    "https://www.youtube.com/watch?v=HSzx-zryEgM")

thor_ragnarok = media.Movie(
    "Thor Ragnarok",
    "A movie about Thor saving Asgard with the Hulk",
    "https://www.flickeringmyth.com/wp-content/upload"
    "s/2017/03/Thor-Ragnarok.jpg",
    "https://www.youtube.com/watch?v=ue80QwXMRHg")

spiderman_homecoming = media.Movie(
    "Spiderman Homecoming",
    "A story about Spiderman agains the Vulture",
    "https://i.redd.it/90o1bvtzs73z.jpg",
    "https://www.youtube.com/watch?v=DiTECkLZ8HM")

guardians_of_the_galaxy2 = media.Movie(
    "Guardians of the Galaxy 2",
    "A story about unique heroes fighting aplanet Celestial God",
    "http://egmnowbeta.s3-us-west-2.amazonaws.com/wp-content/uploads/"
    "2017/02/28221038/Guardians-of-the-Galaxy-Vol-2-New-Poster.jpg",
    "https://www.youtube.com/watch?v=dW1BIid8Osg")

captain_america_civil_war = media.Movie(
    "Captain America Civil War",
    "A story about a group of super heroes at war with each other",
    "https://s-media-cache-ak0.pinimg.com/originals/07/bc/cb/07bccb"
    "732e65f653e87928de34e551a3.jpg",
    "https://www.youtube.com/watch?v=dKrVegVI0Us")

black_panther = media.Movie(
    "Black Panther",
    "A story about a warrior super hero learning to become a king and"
    "a good leader",
    "http://pre08.deviantart.net/512d/th/pre/f/2017/059/2/e/black_pant"
    "her___mock_movie_poster_by_bryanunderwood-db0qo1y.jpg",
    "https://www.youtube.com/watch?v=dxWvtMOGAhw")


movies = [doctor_strange, thor_ragnarok, spiderman_homecoming,
          guardians_of_the_galaxy2, captain_america_civil_war, black_panther]

# This function invokes the list of movie objects as input to create an HTML
# file and open it through the browser.
fresh_tomatoes.open_movies_page(movies)
