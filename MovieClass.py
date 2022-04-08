class Movie:

    # constructor method to create Movie object
    def __init__(self, title, genre, length, cast, director, admin_rating, language, timing, capacity):

        self.title = title
        self.genre = genre
        self.length = length
        self.cast = cast
        self.director = director
        self.admin_rating = admin_rating
        self.language = language
        self.timing = timing
        self.capacity = capacity


    # to print all the details about the movie

    def complete_movie_details(self):
        print("Title : ", self.title)
        print("Genre : ",self.genre)
        print("Casts : ", self.cast)
        print("Length : ", self.length)
        print("Director : ", self.director)
        print("Rating : ", self.admin_rating)
        print("Language : ", self.language)
        print("Show timing :", self.show_timing)
        print("Capacity acc. to screening : ", self.capacity)

    # method to update the movie title
    def edit_movie_title(self, new_name):
        self.title = new_name
        print("MOVIE TITLE UPDATED!1")

    # method to update movie_length
    def edit_movie_length(self, new_length):
        self.length = new_length
        print("MOVIE LENGTH UPDATED!!")

    # method to update movie genre
    def edit_movie_genre(self, new_genre):
        self.genre = new_genre
        print("MOVIE GENRE UPDATED!!")

    # method to update movie casts
    def edit_movie_cast(self, new_cast):
        self.cast = new_cast
        print("MOVIE CASTS UPDATED!!")

    # method to update movie director
    def edit_movie_director(self, new_director):
        self.director = new_director
        print("MOVIE DIRECTOR UPDATED!!")

    # method to update movie rating
    def edit_movie_rating(self, new_rating):
        self.admin_rating = new_rating
        print("MOVIE RATING UPDATED!!")

    # method to update movie language
    def edit_movie_language(self, new_language):
        self.language = new_language
        print("MOVIE LANGUAGE UPDATED!!")

    # method to update movie screening timings
    def edit_movie_timing(self, new_show_timings, temp):
        self.show_timing[temp - 1] = new_show_timings
        print("MOVIE TIMINGS UPDATED!!")

    # method to update theater capacity acc. to screening
    def edit_movie_capacity(self, new_capacity, temp):
        self.capacity[temp - 1] = new_capacity
        print("SEATS ACC. TO SHOW TIMINGS UPDATED!!")
