"""
Description = Program to find the factorial of a number using Recursion.
"""
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)



n = int(input("Enter A Number"))
print(factorial(n))