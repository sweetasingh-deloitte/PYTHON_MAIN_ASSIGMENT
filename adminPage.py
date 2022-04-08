import time
from editMovie import edit_movie
from deleteMovie import delete_movie
from data import *
from MovieClass import Movie



def admin_role():
    while True:
        # Select the choices here
        print("**************WELCOME ADMIN**************")
        print("1. Add New Movie Info ")
        print("2. Edit Movie Info ")
        print("3. Delete Movies ")
        print("4. Exit")
        user_input = int(input("Please enter your choice : "))

        # ADDING NEW MOVIE INFORMATION
        if user_input == 1:
            title = input("Movie title : ")
            genre = input("Movie genre : ")
            length = input("Movie length :")
            cast = input("Movie cast : ")
            director = input("Movie director :")
            admin_rating = int(input("Movie rating from 1 to 10 :"))

            rating_bool = True
            while rating_bool:
                if 1 <= admin_rating <= 10:
                    rating_bool = False
                else:
                    print("Range should be between 1 - 10")

            language = input("Movie language : ")
            show_timing = input("Show timing eg. timing1 ,timings2: ")
            timing = show_timing.split(',')
            no_of_shows = input("Number of Shows in a day: ")
            first_show = input("Enter first show timing: ")
            inta_time = input("Enter interval timing: ")
            gap_btw_shows = input("Gap Between Shows: ")
            capacity_input = input("Capacity per show: eg. 50,60 ")
            capacity = capacity_input.split(',')

            # creating an object of the Movie class
            movie = Movie(title, genre, length, cast, director, admin_rating, language, timing, no_of_shows,first_show,inta_time,gap_btw_shows,capacity)

            # append the created object into movie list that stores all the movies
            movies_list.append(movie)
            print("**************MOVIE ADDED SUCCESSFULLY**************")



            """
            with open("data.txt", "w") as f:
                f.write(title + "," + genre + "," + length + "," + cast + "," + director + "," + str(admin_rating) + "," + language + "," + show_timing + "," + no_of_shows + "," + first_show + "," + interval_time + "," + gap_btw_shows + "," + capacity_input)

                f.close()
            print("----------MOVIE ADDED SUCCESSFULLY!!!----------")
            """

        # editing movie info
        elif user_input==2:
            edit_movie()

        elif user_input == 3:
            delete_movie()

        elif user_input == 4:
            break

        else:
            print("NO NOT VALID: ENTER VALID NUMBER")

