"""
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("You are welcome")


greet("Babalola", "Samuel")
"""
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 4, 4, 5))    