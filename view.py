
def start():
    menu = """
    Welcome to the Terminal Library Management.
    Please enter an option:
    Menu for user:
    1. Register
    2. Login
    3. See the details of books
    4. Exit
    """
    choice = input(menu)
    return choice

def create_account():
    username = input("Hi user, enter your name: ")
    password_1 = input("Enter your password: ")
    password_2 = input("Confirm your password: ")
    mobile = int(input("Enter your mobile number: "))
    if(password_1 == password_2):
        print("Passwords match.")
        return username, password_1, mobile
    else:
        print("Passwords do not match: RETRY!")
        create_account()

def login_prompt():
    mobile = input("Enter your mobile number: ")
    password = input("Enter your password: ")
    return mobile, password

def success_account(user_account):
    print(f"Hi {user_account.username}, your account has been created successfully.")

def success_login(user_account):
    print(f"Hi {user_account.username}, you have logged in successfully.")

def incorrect_choice():
    print("Invalid choice entered.")
    return

def incorrect_credentials():
    print("The credentials entered are incorrect")
    return


def success_account_added(user_account):
    print(f"Hi Librarian, {user_account.username}'s account has been created successfully")


def book_rent():
    rented_book = input("Enter the book name that you want to rent: \n")
    return rented_book
def book_return():
    returned_book = input("Enter the book name that you want to return: \n")
    return returned_book

def rent_return():
    menu = """
    1. Rent a book
    2. Return a book
    3. Exit
    """
    choice = input(menu)
    return choice

def librarian_options(user_account):
    print(f"Hi Librarian {user_account.username}, you have logged in successfully.")
    menu = """
    1. Add a user
    2. Display user details
    3. Update a user
    4. Delete a user
    5. Add a book
    6. Display book details
    7. Update a book
    8. Delete a book
    9. Perform rental and return operations
    10. Exit
    """

    choice = input(menu)
    return choice

def add_user():
    username = input("Hi Enter a username for the account to be created:\n ")
    password_1 = input("Enter the password password: ")
    password_2 = input("Confirm the password: ")
    mobile = int(input("Enter the mobile number: "))
    if (password_1 == password_2):
        print("Passwords match.")
        return username, password_1, mobile
    else:
        print("Passwords do not match: RETRY!")
        add_user()

def display_users(users_dict):
        print("**********************************************************")
        print("{:<15} {:<20} {:<25}".format("USERNAME", "PASSWORD", "MOBILE"))
        print("**********************************************************")

        for user in users_dict:
            print("{:<15} {:<20} {:<25}".format(users_dict[user]["username"], users_dict[user]["password"], user))
        print("**********************************************************")

def update_user():
    mobile = input("Enter the mobile number of the user to fetch the details: \n")
    return mobile

def update_user_old_details(username, password, mobile):
    print("Current username of the user: ", username)
    print("Current password of the user: ", password)
    print("Current mobile number of the user: ", mobile)
    print("Please enter the new details if you wish to change.")
    new_username = input("Enter the new username: \n")
    new_password = input("Enter the new password: \n")
    new_mobile = input("Enter the new mobile number: \n")
    return new_username, new_password, new_mobile, mobile


def delete_user():
    pass

def add_book():
    pass

def display_books(books_dict):

    print("**********************************************************")
    print("{:<15} {:<20} {:<25}".format("BOOK", "AUTHOR", "PUBLISHER"))
    print("**********************************************************")

    for book in books_dict:
        print ("{:<15} {:<20} {:<25}".format(book, books_dict[book]["author"], books_dict[book]["publisher"]))
    print("**********************************************************")
def update_book():
    pass

def delete_book():
    pass
def rental_return():
    pass

def exit():
    print("OUT OF THE APPLICATION")
