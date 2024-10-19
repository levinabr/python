"""
author = levin abraham jacob
Title: Simple desktop calculator using Python. Only the five basic arithmetic operators.
"""

num1 =int(input("enter a number (1)"))
num2 =int(input("enter another number (2)"))
num3 =int(input("enter a 3rd number"))

#addition

print("the sum of number 1 and number  2 is = " ,num1+num2)
#substraction

print("the difference between number 2 and number 1 is =",num2-num1)
#multiplication
print("the product of number 1 and number 2 is =", num1 * num2)
#devision
print("The quotient when num1 is divided by num2 is: " , num1/num2)
#modulus
print("The remainder when num1 is divided by num2 is:  " , num1%num2)
#Combined Arithmetic Operation
z = (num1 + num2) *num3 / 2
print("The result of (num1 + num2) * num3 / 2 is: " , z)
