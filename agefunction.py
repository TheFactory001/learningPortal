# Write an age group function
# List of 100 elements ranging from 1-98.
# Write a function that creates 3 lists with age range 1-33, 34-67, 68-98.

import random

age_range = []
for i in range(1, 98):
    age_range.append(random.randint(1, 98))


def age():
    first_age_group = []
    second_age_group = []
    third_age_group = []
    for numbers in age_range:
        if numbers >= 0 and numbers <= 33:
            first_age_group.append(numbers)
        elif numbers <= 66:
            second_age_group.append(numbers)
        else:
            third_age_group.append(numbers)

    return[first_age_group, second_age_group, third_age_group]


result = age()
print(result)
