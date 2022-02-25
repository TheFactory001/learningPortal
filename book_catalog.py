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


# first we find the user with more than one item
# seller freq stores a seller name as key and number of times listed as key value
seller_freq = {}
for each_bok in book_sellers:
    sellers_name = each_bok["name"]
    if sellers_name in seller_freq:
        seller_freq[sellers_name] += 1
    else:
        seller_freq[sellers_name] = 1  # first occurence

# lehs get the one(s) with more than one item by filtering out
repetition = [each for each in seller_freq if seller_freq[each] > 1]
print(repetition)  # only name with more than an item

# since this example its only a seller that has more than a book
# we know thats just an item and has index of 0-->so its repetition[0]
books = []
comb_price = 0
for each4 in book_sellers:
    if repetition[0] == each4["name"]:
        books.append(each4["book"])
        comb_price += each4["price"]
print(books, comb_price)
