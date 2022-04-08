import time
from registration import register
from adminPage import admin_role
from userActions import user_func

# admin userid and password
admin_user_id = "admin@gmail.com"
admin_password = "admin123"


if __name__ == '__main__':
    while True:
        print("**************WELCOME TO BOOK MY SHOW**************")
        print("1. Login ")
        print("2. Register New account")
        print("3. Exit")
        user_choice1 = int(input("Please enter your choice : "))

        if user_choice1 == 1:
            print("**************WELCOME TO BOOK MY SHOW**************")
            user_name_input = input("Please enter your user ID : ")
            password_input = input("Please enter your Password : ")

            # Split on the space, and store the results in a list of two strings
            for line in open("credentials.txt", "r").readlines():  # Read the lines
                login_info = line.split(",")

            if user_name_input == admin_user_id and password_input == admin_password:
                admin_role()
            elif user_name_input == login_info[0] and password_input == login_info[4]:
                user_func(user_name_input)
            else:
                print("Wrong credentials. Enter correct data!!")

        elif user_choice1 == 2:
            register()

        elif user_choice1 == 3:
            print("**************THANK YOU, PLEASE VISIT AGAIN**************")
            break

        else:
            print("NO NOT VALID: ENTER VALID NUMBER")
