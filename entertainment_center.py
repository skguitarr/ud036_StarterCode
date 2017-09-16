import fresh_tomatoes
import media

#Create a movie instance
rushmore = media.Movie("Rushmore",
                    "A story of a boy genius who makes movies",
                    "https://upload.wikimedia.org/wikipedia/en/4/42/Rushmoreposter.png",
                    "https://www.youtube.com/watch?v=GxCNDpvGyss")

#Create a movie instance
amadeus = media.Movie("Amadeus",
                    "A story of a boy genius who writes classial music",
                    "https://upload.wikimedia.org/wikipedia/en/2/2f/Amadeusmov.jpg",
                    "https://www.youtube.com/watch?v=3qikgX4rlG4")

#Create a movie instance
theBigLebowski = media.Movie("The Big Lebowski",
                    "A story of a dude and a glimpse into his world",
                    "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                    "https://www.youtube.com/watch?v=cd-go0oBF4Y")

#Create a movie instance
guardiansOfTheGalaxy2 = media.Movie("Guardians of the Galaxy 2",
                    "A story of a dude and a glimpse into his world",
                    "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                    "https://www.youtube.com/watch?v=duGqrYw4usE")

#Create a movie instance
theThreeAmigos = media.Movie("The Three Amigos",
                    "A story of 3 actor friends who find out what happens when acting meets wild west reality",
                    "https://upload.wikimedia.org/wikipedia/en/8/87/Three_amigos_ver2.jpg",
                    "https://www.youtube.com/watch?v=g9OAjqs6dOo")

#Create a movie instance
rioBravo = media.Movie("Rio Bravo",
                    "Classic western movie starring John Wayne who along with his friends and allies protect a town from a gang who wants what they have",
                    "https://upload.wikimedia.org/wikipedia/en/7/7a/Riobravoposter.jpg",
                    "https://www.youtube.com/watch?v=WPO12ZzGS84")

#Create the movie array for open_movies_page to process and place in the HTML
movies = [rushmore, amadeus, theBigLebowski, guardiansOfTheGalaxy2, theThreeAmigos, rioBravo];

#Pass the movies array to the open_movies_page
fresh_tomatoes.open_movies_page(movies)
