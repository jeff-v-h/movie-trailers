import fresh_tomatoes
import media

forrest_gump = media.Movie("Forrest Gump",
                        "Slow-witted Forrest Gump tells his eventful life story",
                        "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                        "https://www.youtube.com/watch?v=bLvqoHBptjg")

#print(toy_story.storyline)
the_lion_king = media.Movie("The Lion King",
                     "A young lion's journey to become King",
                     "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                     "https://www.youtube.com/watch?v=4sj1MT05lAA")
#print(avatar.storyline)
#avatar.show_trailer()
the_shawkshank_redemption = media.Movie("The Shawshank Redemption", "A man's survivial in prison",
                             "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                             "https://www.youtube.com/watch?v=6hB3S9bIaco")

ex_machina = media.Movie("Ex Machina", "A programmer has been tasked to test how human-life a robot is",
                          "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
                          "https://www.youtube.com/watch?v=PI8XBKb6DQk")

i_am_sam = media.Movie("I Am Sam", "Daughter and mentally disabled father fighting to stay together as a family",
                                "http://img.moviepostershop.com/i-am-sam-movie-poster-2001-1020204010.jpg",
                                "https://www.youtube.com/watch?v=ir6_2EkhzAc")

the_dark_knight = media.Movie("The Dark Knight", "Vigilante Batman fights The Joker to save Gotham City",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [forrest_gump, the_lion_king, the_shawkshank_redemption, ex_machina, i_am_sam, the_dark_knight]
fresh_tomatoes.open_movies_page(movies)
