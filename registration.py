def register():
    """
    creating new account here
    @name name of the user
    @email email of the user
    @phone_number phone number of the user
    @age age of the user
    @password password of the user
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
