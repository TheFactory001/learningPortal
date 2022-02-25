from webbrowser import get

# catalogue of booksellers
book_sellers = [
    {"name": "Robert", "book": "Rich Dad", "price": 1500},
    {"name": "Dan", "book": "money principles", "price": 2600},
    {"name": "Malcom", "book": "success stories", "price": 1700},
    {"name": "Obama", "book": "Stories my dad", "price": 1300},
    {"name": "Mosh", "book": "let's code", "price": 5000},
    {"name": "Enith", "book": "one time free", "price": 2500},
    {"name": "Ken", "book": "Heart is free", "price": 900},
    {"name": "Awolowo", "book": "Once upon a Nigeria", "price": 2300},
    {"name": "Drook", "book": "Dark magic", "price": 2000},
    {"name": "Robert", "book": "Poor Dad", "price": 1900},
    {"name": "Steve", "book": "behind the hidden walls", "price": 800}
]
# sort the list using price
book_sellers.sort(key=lambda each_seller: each_seller["price"])
# after sorting in ascending, cheapest book would be first in the list
cheapest_book = (book_sellers[0])["book"]
print("cheapest book is: ", cheapest_book)
# most expensive is last
expensive_book = (book_sellers[-1])["book"]
print("most_expensive book is: ", expensive_book)

# average price is total/no.
total_price = 0
no_of_books = len(book_sellers)
for each_book in book_sellers:
    price = each_book["price"]
    total_price += price
average_price = total_price/no_of_books
print("average price of books in your catalougue is", average_price)

# a function that returns list of books by a specified seller and the combined price of the user


def seller_listing(sellers_name):
    seller_detils = [
        ele for ele in book_sellers if ele["name"] == sellers_name]
    sellers_books = [ele["book"] for ele in seller_detils]
    total = 0
    for ele in seller_detils:
        total += ele["price"]
    if not sellers_books:
        return ("no listing was found for this name")
    return f" Books by {sellers_name} are {sellers_books},all cost {total}"


print(seller_listing("Robert"))
