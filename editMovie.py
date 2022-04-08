from data import *

def edit_movie():
    print("**************EDIT MOVIE INFO**************")
    print("**************List of available movies**************")
    for i in movies_list:
        print("   ", i.title)

    print()
    edit_movie_name = input("Enter Movie name to be edited : ")

    success_flag = False

    # Itreating through the list to find if entered movie is present or not
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
            print("7. To edit language")
            print("9. To edit capacity")

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
                print("Current language : {}".format(i.language))
                new_language = input("Please enter new language : ")
                i.edit_movie_language(new_language)

            elif edit_option == 8:
                print("Current show timings : {}".format(i.show_timing))
                print("-----------Available show timings--------")

                # print all the available shows
                for show_time in i.show_timing:
                    print(show_time)
                # ask user to select which show timing need to be updated
                temp = int(input("Enter which timings need to be updated  : "))
                new_show_timing = input("Please enter new show timings : ")

                # call edit_movie_timing method in Movie class to update the show timings
                i.edit_movie_timing(new_show_timing, temp)

            elif edit_option == 9:
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
            print("PLEASE ENTER CORRECT MOVIE NAME !!")




















