'''
for number in range(1, 9, 2):
    print("Attempt", number, (number + 1) * ".")
'''
successful = "Zero"
for number in range(3):
    print("Attempt")
    if successful:
        print("Successsful") 
        break
else:
    print("Attempted 3 times and failed")       