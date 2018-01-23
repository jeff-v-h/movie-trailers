import fresh_tomatoes
import media


# Forrest Gump movie: movie title, poster image and movie trailer
forrest_gump = media.Movie(
    "Forrest Gump",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg")

# Lion King movie: movie title, poster image and movie trailer
the_lion_king = media.Movie(
    "The Lion King",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
    "https://www.youtube.com/watch?v=4sj1MT05lAA")

# Shawshank Redemption movie: movie title, poster image and movie trailer
the_shawkshank_redemption = media.Movie(
    "The Shawshank Redemption",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

# Ex Machina movie: movie title, poster image and movie trailer
ex_machina = media.Movie(
    "Ex Machina",
    "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
    "https://www.youtube.com/watch?v=sNExF5WYMaA")

# I Am Sam movie: movie title, poster image and movie trailer
i_am_sam = media.Movie(
    "I Am Sam",
    "http://img.moviepostershop.com/i-am-sam-movie-poster-2001-1020204010.jpg",
    "https://www.youtube.com/watch?v=_A7N1a7TPbI")

# The Dark Knight movie: movie title, poster image and movie trailer
the_dark_knight = media.Movie(
    "The Dark Knight",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=TQfATDZY5Y4")

# Set the movies that will be passed to the media file
movies = [forrest_gump, the_lion_king, the_shawkshank_redemption, ex_machina,
          i_am_sam, the_dark_knight]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
