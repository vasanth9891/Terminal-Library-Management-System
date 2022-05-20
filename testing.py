import json
with open("users.json", "r+") as f:
    users_dict = json.load(f)
    print(users_dict)
    print(type(users_dict))

with open("books.json", "r+") as f:
    books_dict = json.load(f)
    print(books_dict)
    # print(type(books_dict))
    # print(books_dict["C language"])
    # print(books_dict.keys())
    # print(books_dict["C language"]["author"])
    # print(books_dict["C language"]["publisher"])
    #
    # for book in books_dict:
    #     print(book)
    #     print(books_dict[book]["author"])
    #     print(books_dict[book]["publisher"])
    #     print()


with open("users.json", "r+") as f:
    users_dict = json.load(f)

    for k in users_dict.keys():
        print(k)
    # print(users_dict.keys())
    n = 1234567890
if n in users_dict.keys():
    print("It is available.")
else:
    print("It is not available.")
