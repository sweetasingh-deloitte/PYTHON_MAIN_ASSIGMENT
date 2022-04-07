import time



def admin_role():
    while True:
        #Select the choices here
        print("---------- Welcome Admin ----------")
        print("1. Add New Movie Info ")
        print("2. Edit Movie Info ")
        print("3. Delete Movies ")
        print("4. Exit")
        user_input = int(input("Please enter your choice : "))


        #user select option 1
        if user_input == 1:
            title = input("Movie title : ")
            genre = input("Movie genre : ")
            length = int(input("Movie length :"))
            cast = input("Movie cast : ")
            director = input("Movie director :")

            rating_flag = True
            while rating_flag:
                admin_rating = int(input("Movie rating from 1 to 10 :"))
                if 1 <= admin_rating <= 10:
                    rating_flag = False
                else:
                    print("Range should be between 1 - 10")

            language = input("Movie language : ")
            show_timing = input("Show timing eg. timing1 ,timings2: ")
            timing = show_timing.split(',')
            no_of_shows = int(input("Number of Shows in a day: "))
            first_show = input("Enter first show timing: ")
            interval_time = input("Enter interval timing: ")
            gap_btw_shows = input("Gap Between Shows: ")
            capacity_input = input("Capacity per show: eg. 50,60 ")
            capacity = capacity_input.split(',')

            # create an object of the Movie class
            movie = Movie(title, genre, length, cast, director, admin_rating, language, timing, capacity)
            # append the created object into movie list which stores all the movies
            movies_list.append(movie)
            print("----------MOVIE ADDED SUCCESSFULLY!!!----------")

