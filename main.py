# import movie class and prerolled movie website generator
import fresh_tomatoes
import movie

# data for each of the movies to display
movie_data = [
	[
	'The Matrix'
	,'http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle'
	,'https://www.youtube.com/watch?v=a94b1yZOBes'
	]
	,[
	'Zoolander'
	,'http://t2.gstatic.com/images?q=tbn:ANd9GcTSNVaidBcksRzbIxrYyxm-5Oyy_Z5ncdEcvR4R2sz8nzu1jg19'
	,'https://www.youtube.com/watch?v=YtQq0T3ExLs'
	]
	,[
	'Mr. Baseball'
	,'http://www.gstatic.com/tv/thumb/movieposters/14265/p14265_p_v8_aa.jpg'
	,'https://www.youtube.com/watch?v=uN_H71V6kZY'
	]
	,[
	'The Martian'
	,'http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ'
	,'https://www.youtube.com/watch?v=XQnYm5MG1x0'
	]
	,[
	'A View To A Kill'
	,'https://resizing.flixster.com/4uTSDHPNEj3XP9VyaChnvs7dhq8=/206x305/v1.bTsxMTIwNDg3MztqOzE3Mjc0OzEyMDA7OTAwOzEyMDA'
	,'https://www.youtube.com/watch?v=PKsr5yrxE-k'
	]
]

# it's a list comprehension to create a list of Movie instances, wow!
movie_list = [movie.Movie(data) for data in movie_data]

# pass the movie_list to open_movie_pages to generate the page
fresh_tomatoes.open_movies_page(movie_list)