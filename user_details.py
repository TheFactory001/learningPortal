
# dictionary that has name, phonenumber and age
dict_list = [
    {"name": "Daniel", "age": 24, "phone_number": "+2349039074767"},
    {"name": "Mike", "age": 25, "phone_number": "+2349039074767"},
    {"name": "Judah", "age": 18, "phone_number": "+2349039074767"},
    {"name": "Dennis", "age": 30, "phone_number": "+2349039074767"},
    {"name": "Truth", "age": 29, "phone_number": "+2349039074767"},
    {"name": "Onfroy", "age": 22, "phone_number": "+2349039074767"},
    {"name": "Wayne", "age": 36, "phone_number": "+2349039074767"},
    {"name": "Justice", "age": 26, "phone_number": "+2349039074767"},
    {"name": "Jaden", "age": 12, "phone_number": "+2349039074767"},

]
# sort list by age, descending
dict_list.sort(key=lambda user: user["age"], reverse=True)
# now a sorted list
print(dict_list)

user_names = [user["name"] for user in dict_list]
print(user_names)

"""
# new user
new_user = {"name": "Lisa", "age": 32, "phone_number": "+2349039074767"}
user_dennis = {"name": "Dennis", "age": 26, "phone_number": "+2347054729247"}

def append_user(new_user):
    for users in dict_list:
        if users["name"] == new_user["name"]:
            suggested_name = new_user["name"] + str(new_user["age"])
            raise ValueError(
                f"User not registered: This username already exists, try {suggested_name}")
    dict_list.append(new_user)


try:
    append_user(user_dennis)
except ValueError as msg:
    print(msg)

"""
# code2
# a case whereby a new user is to added, we tryna keep unique names/username
# new users
user_lisa = {"name": "Lisa", "age": 32, "phone_number": "+2349039074767"}
user_dennis = {"name": "Dennis", "age": 26, "phone_number": "+2347054729247"}


def append_user(new_user):
    new_user_name = new_user["name"]
    for users in dict_list:
        if users["name"] == new_user["name"]:  # name not unique
            suggested_name = new_user["name"] + str(new_user["age"])

            print(
                f"User not registered: {new_user_name} already exists, try {suggested_name}")  # do not save
            return None
    dict_list.append(new_user)  # else, save user
    print("Your Details have been saved", new_user["name"])


append_user(user_dennis)
append_user(user_lisa)
print(dict_list)
