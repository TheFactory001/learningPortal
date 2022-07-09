#for number in range(10):
    #print(number)
#Write a program to print natural numbers in descending order using a while loop
def print_natural_number(natural_number):
    while natural_number > 0:
        print(natural_number)
        natural_number = natural_number - 1


#print_natural_number(20)

def print_multiple(number):
    new_number = 0
    while new_number <= (number // 2):
        print(new_number * 2)
        new_number = new_number + 1


#print_multiple(10)        

def multiply(number):
    for i in range(number + 1):
        if(i % 2 == 0):
            print(i)
            

multiply(10)            