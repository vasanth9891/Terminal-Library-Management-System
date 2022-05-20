import json

class user_account:
    def __init__(self, username, password, mobile):
        self.username = username
        self.password = password
        self.mobile = mobile

    @classmethod
    def create_account(cls, username, password, mobile):
        with open("users.json", "r+") as f:
            users_dict = json.load(f)
            
        while mobile in users_dict.keys():
            mobile = mobile
        user_acc = user_account(username, password, mobile)
        user_acc.save()
        return user_acc

    @classmethod
    def login(cls, mobile, password):
        with open("users.json", "r+") as f:
            users_dict = json.load(f)
        if mobile in users_dict and password == users_dict[mobile]["password"]:
            username = users_dict[mobile]["username"]
            user_acc = user_account(username, password, mobile)
            user_acc.save()
            return user_acc
        else:
            return False

    @classmethod
    def users_details(cls):
        with open("users.json", "r+") as f:
            users_dict = json.load(f)
            return users_dict

    @classmethod
    def update_user(cls, mobile):
        with open("users.json", "r+") as f:
            users_dict = json.load(f)
            if mobile in users_dict:
                username = users_dict[mobile]["username"]
                password = users_dict[mobile]["password"]
        return username, password, mobile

    @classmethod
    def update_user_save(cls, new_username, new_password, new_mobile, old_mobile):
        with open("users.json", "r+") as f:
            users_dict = json.load(f)
            if old_mobile in users_dict:
                users_dict[old_mobile] = new_mobile
                users_dict[old_mobile]["username"] = new_username
                users_dict[old_mobile]["password"] = new_password
        return

    @classmethod
    def books_details(cls):
        with open("books.json", "r+") as f:
            books_dict = json.load(f)
            return books_dict

    @classmethod
    def del_book(cls, rented_book):
        with open("books.json", "r+") as f:
            books_dict = json.load(f)
            # rented_dict = {}
            # rented_dict[rented_book] = {"author"}
            # books_dict2 = books_dict
            del books_dict[rented_book]
        with open("books.json", "w+") as f:
            json.dump(books_dict, f, indent=3)
        return

    def save(self):
        with open("users.json", "r+") as f:
            users_dict = json.load(f)
        users_dict[self.mobile] = {"username":self.username,"password":self.password}

        with open("users.json", "w+") as f:
            json.dump(users_dict, f, indent=3)
        return




#     def deposit_money(self,deposit):
#         self.balance+=deposit
#         self.save()
#         return True 

#     def withdrawal(self,withdraw_money):
#         if withdraw_money<=self.balance:
#             self.balance-=withdraw_money
#             self.save()
#             return True 
#         else:
#             return False