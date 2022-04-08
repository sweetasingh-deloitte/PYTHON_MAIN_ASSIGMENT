import time

def admin_role():
    while True:
        #Select the choices here
        print("**************WELCOME ADMIN**************")
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
            capacity_input = input("Capacity per show: ")

            with open("data.txt", "w") as f:
                f.write(title + "," + genre + "," + length + "," + cast + "," + director + "," + admin_rating + "," + language + "," + timing + "," + no_of_shows + "," + first_show + "," + interval_time + "," + gap_btw_shows + "," + capacity_input)
                f.close()
                print("You have registered successfully!")



"""
        elif user_input==2:
            print("----------EDIT MOVIE INFO ----------")
            print("-------List of available movies----- ")
            for i in movies_list:
                print("   ", i.title)

            print()
            edit_movie_name = input("Enter Movie name to be edited : ")

            success_flag = False

            # iterate thought the movies list to find if entered movie name present in the list
            for i in movies_list:

                # if movie name is present in the list
                if i.title == edit_movie_name:
                    success_flag = True
                    # i.complete_movie_details()
                    print("------------EDIT OPTIONS ------------")
                    print("1 . To edit title ")
                    print("2 . To edit genre")
                    print("3 . To edit length ")
                    print("4 . To edit cast")
                    print("5.  To edit director ")
                    print("6. To edit rating ")
                    print("7. To edit show_timing")
                    print("8. To edit capacity")

                    edit_option = int(input("Please enter your edit option : "))
                    if edit_option == 1:
                        print("Current title : {}".format(i.title))
                        new_title = input("Please enter new movie title :")
                        i.edit_movie_title(new_title)

                    elif edit_option == 2:
                        print("Current genre : {}".format(i.genre))
                        new_genre = input("Please enter new genre type :")
                        i.edit_movie_genre(new_genre)

                    elif edit_option == 3:
                        print("Current length : {}".format(i.length))
                        new_length = int(input("Please enter new movie length :"))
                        i.edit_movie_length(new_length)

                    elif edit_option == 4:
                        print("Current cast : {}".format(i.cast))
                        new_cast = input("Please enter new movie cast : ")
                        i.edit_movie_cast(new_cast)

                    elif edit_option == 5:
                        print("Current director : {}".format(i.director))
                        new_director = input("Please enter new movie director :")
                        i.edit_movie_director(new_director)

                    elif edit_option == 6:
                        print("Current rating : {}".format(i.admin_rating))
                        rating_flag = True
                        while rating_flag:
                            new_rating = int(input("Please enter new rating [1,10] :"))
                            if 1 <= new_rating <= 10:
                                rating_flag = False
                            else:
                                print("Range should be between 1 - 10")
                        i.edit_movie_rating(new_rating)


        elif edit_option == 7:
                        print("Current show timings : {}".format(i.show_timing))
                        print("-------Available show timings--------")

                        # print all the available shows
                        for show_time in i.show_timing:
                            print(show_time)
                        # ask user to select which show timing need to be updated
                        temp = int(input("Enter which timings need to be updated  : "))
                        new_show_timing = input("Please enter new show timings : ")

                        # call edit_movie_timing method in Movie class to update the show timings
                        i.edit_movie_timing(new_show_timing, temp)

                    elif edit_option == 8:
                        # print("Current capacity per show : {}".format(i.capacity))
                        print("Available seats acc. to show timings ")
                        # print all the available seats acc. to the show timings
                        for z in range(0, len(i.capacity)):
                            print(" {} show -  Total seats available : {} ".format(i.show_timing[z], i.capacity[z]))

                        # ask user to select for which show timings capacity need to be changed/updated
                        temp = int(input("Enter which show capacity need to be updated"))
                        new_capacity = int(input("Please enter new capacity :"))

                        # call edit_movie_capacity in Movie class to update the movie capacity acc. to show timings
                        i.edit_movie_capacity(new_capacity, temp)



                    else:
                        print("INVALID INPUT, PLEASE SELECT CORRECT OPTIONS")

            if not success_flag:
                print("PLEASE ENTER CORRECT MOVIE NAME/TITLE !!")

"""