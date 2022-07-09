"""
# print(6 + (6**2) + (6**3))
# print((7 + 7 + 7) * 3)
num = int(input("enter any number:"))
#num = 346
# if number = 35:
    # number divided by 2, remainder is 1
   # number = 78:
if (num%2) == 0:
    print("It is an even number")
else:
    print("It is an odd number") 
    """
   # Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
a = 2
b = 2
c = 2
sum = (a + b + c)
print("sum = ", sum)
#if the values are equal then return three times of their sum.
if a==b==c:
    print(3 * (sum))