# Write a function that takes a list and a number as arguments (e.g def remove_target(my list, target)).
#The function removes target from the list. If target value does not exist, return -1
def remove_target(numbers, target):
    if target in numbers:
        numbers.remove(target)
        print(numbers)
    else:
        print("Numbers does not exist")

numbers= [23, 44, 16]
remove_target(numbers, 56)
       