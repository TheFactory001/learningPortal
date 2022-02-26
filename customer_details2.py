# function to check if a customer already exists
customer_details = [
    {"name": "Abbey", "age": 22, "phone_number": "08142558601"},
    {"name": "Adebola", "age": 25, "phone_number": "09076263857"},
    {"name": "Bayo", "age": 19, "phone_number": "08183150272"},
    {"name": "Bello", "age": 23, "phone_number": "08105233549"},
    {"name": "Christy", "age": 29, "phone_number": "08055291892"},
    {"name": "Cole", "age": 32, "phone_number": "08160862107"},
    {"name": "Doyin", "age": 16, "phone_number": "09014464895"},
    {"name": "Jessie", "age": 43, "phone_number": "08114805552"},
    {"name": "Joyce", "age": 26, "phone_number": "08102914941"},
    {"name": "Mariam", "age": 30, "phone_number": "09035358581"},
    {"name": "Adebola", "age": 25, "phone_number": "09076263857"},
]

new_user = {"name": "Joyce", "age": 24, "phone_number": "08149068399"}
user_found = False
for user in customer_details:
    # print(user["name"])
    if (user["name"] == new_user["name"]):
        print(user["name"], "already exists")
        user_found = True

if user_found == False:
    customer_details.append(new_user)
print(customer_details)
