class UserInfo:
    """
    creating new account here
    @name name of the user
    @email email of the user
    @phone_number phone number of the user
    @age age of the user
    @password password of the user
    """

    # constructor method to create an object of User
    def __init__(self, name, email, phone_number, age, password):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.age = age
        self.password = password
        # store all the movies booked by the user in the format of [movie_name, show_timing, number_of_seats]
        self.movies_booked = []

"""
    print("**************CREATE NEW ACCOUNT*************")
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone_no = input("Enter phone number: ")
    age = input("Enter age: ")
    password = input("Enter password: ")

    with open("credentials.txt", "w") as f:
        f.write(name + "," + email + "," + phone_no + "," + age + "," + password)
        f.close()
        print("You have registered successfully!")
        """
