import random

topList = []
for i in range(0, 100):
    topList.append(random.randint(0,98))

def grouper():
    #Group
    lessThan33 = []
    greaterThan33 = []
    greaterThan67 = []
    for element in topList:
        if element >= 0 and element <= 33:
            lessThan33.append(element)
        elif element >= 34 and element <= 66:
            greaterThan33.append(element)
        else:
            greaterThan67.append(element)
    return [lessThan33, greaterThan33, greaterThan67]


def grouper2():
    # A more comprehensive example
    lessThan33 = sorted([element for element in topList if element >= 0 and element <= 33])
    greaterThan33 = sorted([element for element in topList if element >= 34 and element <= 66])
    greaterThan67 = sorted([element for element in topList if element >= 67])

    return [lessThan33, greaterThan33, greaterThan67]

result = grouper2()
print(result)