# function to get the list of customer details from oldest to youngest
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
    {"name": "Mariam", "age": 30, "phone_number": "09035358581"}
]
# using sorted and lambda to print list sorted
# by age in descending order (oldest to youngest)
print("The list of customer details from the oldest to youngest: ")
print(sorted(customer_details, key=lambda i: i['age'], reverse=True))
customer_details.sort(key=lambda age_gap: age_gap["age"])
oldest_customer = (customer_details[-1])["age"]
print("The oldest_customer is: ", oldest_customer)
youngest_customer = (customer_details[0])["age"]
print("The youngest customer is: ", youngest_customer)
