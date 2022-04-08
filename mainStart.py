import time
from registration import UserInfo
from adminPage import admin_role
from userActions import user_func
from data import *
from MovieClass import Movie

# admin userid and password
admin_user_id = "admin"
admin_password = "admin123"


if __name__ == '__main__':

    # demo Movie data
    movie_demo = Movie("rockstar", "sad", 120, "ranbir kappor", "ali", 5, "hindi", ["7-3", "9-3"], [20, 20])
    movie_demo2 = Movie("iron man", "action", 250, "robert Jr.", "jkhh", 10, "English", ["7-3", "9-3"], [20, 20])
    movies_list.append(movie_demo)
    movies_list.append(movie_demo2)

    # demo User data
    user_demo = UserInfo("sweeta pal", "sweeta@gmail.com", "84563772728", 21, "sweeta@123")
    users_list.append(user_demo)

    while True:
        print("**************WELCOME TO BOOK MY SHOW**************")
        print("1. Admin Login ")
        print("2. User login")
        print("3. Register New account")
        print("4. Exit")
        user_choice1 = int(input("Please enter your choice : "))

        if user_choice1 == 1:
            print("**************WELCOME TO BOOK MY SHOW**************")
            user_name_input = input("Please enter your user ID : ")
            password_input = input("Please enter your Password : ")

            if user_name_input == admin_user_id and password_input == admin_password:
                admin_role()

            else:
                print("PLEASE ENTER CORRECT CREDENTIALS !!")

        elif user_choice1 == 2:
            print("---------------WELCOME TO BOOK MY SHOW-------------")
            print("-------------------USER LOGIN -----------------")
            user_name_input = input("Email Id : ")
            password_input = input("Password  : ")

            successful_login_flag = False
            for i in users_list:

                if i.email == user_name_input and i.password == password_input:
                    successful_login_flag = True
                    user_func(i)

            if not successful_login_flag:
                print("PLEASE ENTER CORRECT CREDENTIALS !!")

        elif user_choice1 == 3:
            print("------------------WELCOME TO BOOK MY SHOW---------------")
            print("----------------------REGISTRATION-------------")
            name = input("Please enter your name                 : ")
            email = input("Please enter your email-id            :")
            phone_number = input("Please enter your phone number : ")
            age = int(input("Please enter your age               : "))
            password = input("Please enter your password         : ")
            # create new user object
            user = UserInfo(name, email, phone_number, age, password)
            # store it into all users details list
            users_list.append(user)
            print("-----------------SUCCESSFUL REGISTRATION--------------------")

        elif user_choice1 == 4:
            print("**************THANK YOU, PLEASE VISIT AGAIN**************")
            break

        else:
            print("NO NOT VALID: ENTER VALID NUMBER")
