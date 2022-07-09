
items = [
    ("Product1", 20),
    ("Product2", 18),      
    ("Product3", 13),
]

def sort_item_key(item):
    return item[1]

def sort_item(items):
    items.sort(key=sort_item_key)
    print(items)

sort_item(items)
