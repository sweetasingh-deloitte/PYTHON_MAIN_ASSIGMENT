from data import movies_list


def user_func(user):
    while True:
        print("**************WELCOME {}**************".format(user.name.upper()))
        print("1 . Book tickets")
        print("2 . Cancel tickets")
        print("3 . give user rating")
        print("4 . Logout ")

        user_input = int(input("Please enter your choice : "))
        if user_input == 1:
            print("----MOVIES PLAYING IN THEATER-----------")
            for i in movies_list:
                print(i.title)
            current_movie = None

            temp_flag = True
            while temp_flag:
                movie_ticket_name = input("Enter the name of the movie to book ticket : ")
                for j in movies_list:

                    if j.title == movie_ticket_name:
                        current_movie = j
                        temp_flag = False
                        break
                else:
                    print("Please enter correct movie name !!")

            print("-----------------------{} MOVIE INFO--------------------".format(current_movie.title.upper()))

            # called complete_movie_details() method from Movie class to print complete details about the movie
            current_movie.complete_movie_details()

            # # print all the available show timings
            # for j in current_movie.show_timing:
            #     print(j)

            movie_timing_input = int(input("Please select the show timing :"))
            total_available_seats = int(current_movie.capacity[movie_timing_input - 1])
            print("Number of seats available for selected timing : {}".format(total_available_seats))

            total_seats_selected = int(input("Please enter the number of seats to be booked  : "))
            if total_seats_selected <= total_available_seats:
                print("TICKET BOOKED, ENJOY THE MOVIE !!!")
                current_movie.capacity[movie_timing_input - 1] -= total_seats_selected
                # user.movies_booked.append({current_movie.title: total_seats_selected})
                user.movies_booked.append(list([current_movie.title, total_seats_selected, movie_timing_input]))
            else:
                print("PLEASE REDUCE THE NUMBER OF SEATS !!")

        elif user_input == 2:

            if len(user.movies_booked) == 0:
                print("NO MOVIE BOOKED TILL NOW!!")
                continue

            print("LIST OF BOOKED MOVIES")
            # for i in range(0, len(user.movies_booked)):
            #     for key, value in user.movies_booked[i].items():
            #         print("{} - seats booked : {}".format(key, value))
            #
            # cancel_movie_name = input("Enter the name of movie whose tickets need to be cancelled ")
            #
            # for i in range(0, len(user.movies_booked)):
            #     for key, value in user.movies_booked[i].items():
            #         if key == cancel_movie_name:
            #             del user.movies_booked[i]

            for i in user.movies_booked:
                print("{} - seats booked : {}".format(i[0], i[1]))

            cancel_movie_name = input("Enter the name of movie whose tickets need to be cancelled :  ")

            index_to_delete = None
            seats = None
            timing = None
            for i in range(0, len(user.movies_booked)):

                if user.movies_booked[i][0] == cancel_movie_name:
                    index_to_delete = i
                    seats = user.movies_booked[i][1]
                    timing = user.movies_booked[i][2]
                    break

            for i in movies_list:

                if i.title == cancel_movie_name:

                    for j in range(0, len(i.capacity)):

                        if j == timing - 1:
                            i.capacity[j] += seats

            del user.movies_booked[index_to_delete]
            print("MOVIE TICKET CANCELLED")

        elif user_input == 3:

            for i in user.movies_booked:
                print(i[0])

            if len(user.movies_booked) == 0:
                print("NO MOVIE BOOKED TILL NOW!!")

        elif user_input == 4:
            print("--------BYEE, LOGOUT-----------")
            break

        else:
            print("----PLEASE SELECT CORRECT OPTIONS!!-----")
