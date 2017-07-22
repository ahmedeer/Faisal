
import fresh_tomatoes
import media
toy_story = media.Movie("Toy Story","Story about a toys","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

john_English_Reborn=media.Movie("Johnny English Reborn","Johnny English upsets gangs","https://upload.wikimedia.org/wikipedia/en/6/6c/Johnny_English_Reborn_Poster.jpg","https://www.youtube.com/watch?v=LOSZLgzgnBs")

breaking_bad=media.Movie("Breaking Bad", "school teacher turn meth gig","https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png","https://www.youtube.com/watch?v=HhesaQXLuRY")

captain_philip=media.Movie("Captain phillips","Surviver thriller on how Navy Seals rescued a ship crew from pirates","https://upload.wikimedia.org/wikipedia/en/a/a8/Captain_Phillips_Poster.jpg","https://www.youtube.com/watch?v=pV-ptQX-75Y")


movies=[toy_story,john_English_Reborn,breaking_bad,captain_philip]

fresh_tomatoes.open_movies_page(movies)
