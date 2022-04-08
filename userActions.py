def user_func(user_name_input):
    while True:
        print("**************WELCOME {}**************".format(user_name_input.name.upper()))
        print("1 . Book tickets")
        print("2 . Cancel tickets")
        print("3 . Movie Booked Details")
        print("4 . Logout ")

        user_input = int(input("Please enter your choice : "))
        #if user_input == 1: