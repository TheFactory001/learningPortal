# python program to sort a list using the length of elements
def sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2


lst = ["Hello", "Available", "Van"]
print(sorting(lst))
