# Terminal Library Management Application
import model, view
import logging
# Create and configure logger
logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='a')

# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

def onboard():
    """
    Welcome to the Terminal Library Management.
    Please enter an option:
    Menu for user:
    1. Register
    2. Login
    3. See the details of books
    4. Exit
    """
    choice = None
    if choice != 3:
        choice = view.start()
        logger.info(f"The choice selected by the user is {choice}")
        if choice == "1":
            username, password, mobile = view.create_account()
            user_account = model.user_account.create_account(username, password, mobile)
            view.success_account(user_account)
            logger.info(f"An account has been created for user {user_account.username}")
            onboard()
        elif choice == "2":
            mobile, password = view.login_prompt()
            logger.info(f"Mobile number entered for login is {mobile} and password is {password}")
            user_account = model.user_account.login(mobile, password)
            if (user_account.mobile == "7904796517" and password == "123"):
                choice = None
                if choice != 10:
                    choice = view.librarian_options(user_account)
                    if choice == "1":
                        username, password, mobile = view.add_user()
                        user_account = model.user_account.create_account(username, password, mobile)
                        view.success_account_added(user_account)
                    elif choice == "2":
                        users_dict = model.user_account.users_details()
                        view.display_users(users_dict)
                    elif choice == "3":
                        mobile = view.update_user()
                        username, password, mobile = model.user_account.update_user(mobile)
                        new_username, new_password, new_mobile, old_mobile = view.update_user_old_details(username, password, mobile)
                        model.user_account.update_user_save(new_username, new_password, new_mobile, old_mobile)
                    elif choice == "4":
                        pass
                    elif choice == "5":
                        pass
                    elif choice == "6":
                        pass
                    elif choice == "7":
                        pass
                    elif choice == "8":
                        pass
                    elif choice == "9":
                        pass
                    elif choice == "10":
                        view.exit()
                    else:
                        logging.warning(f"Invalid choice selected--> {choice}")
                        view.incorrect_choice()
                        view.librarian_options(user_account)
            else:
                view.success_login(user_account)
                logger.info(f"Successful login with mobile number {mobile}")
            while(user_account) == False:
                logging.error(f"Invalid credentials entered: mobile -->{mobile} and password --> {password}")
                view.incorrect_credentials()
                mobile, password = view.login_prompt()
                user_account = model.user_account.login(mobile, password)
                #librarian(user_account)
                onboard()

        elif choice == "3":
            books_dict = model.user_account.books_details()
            view.display_books(books_dict)

            choice = view.rent_return()
            if choice == "1":
                rented_book = view.book_rent()
                model.user_account.del_book(rented_book)
                books_dict = model.user_account.books_details()
                view.display_books(books_dict)

            elif choice == "2":
                returned_book = view.book_return()
            # onboard()

        elif choice == "4":
            view.exit()
        else:
            logging.warning(f"Invalid choice selected--> {choice}")
            view.incorrect_choice()
            onboard()

def librarian(user_account):
    pass
# def transactions(acc):
    '''
    1. check balance
    2. deposit
    3. withdraw
    4. Logout
    '''
    # choice=None
    # while choice!=4:
    #     choice=view.transactions_options()
    #     if choice=='1':
    #         view.display_balance(acc)
    #     elif choice=='2':
    #         deposit=view.get_deposit()
    #         status=acc.deposit_money(deposit) # doubt
    #     elif choice=='3':
    #         withdraw=view.get_withdrawal()
    #         status=acc.withdrawal(withdraw) # doubt
    #     elif choice=='4': # doubt
    #         return 
    #     else:
    #         view.incorecct_choice()
    #         transactions(acc)


onboard()
