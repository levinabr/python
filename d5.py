"""program to find greatest and smallest number"""
n = int(input ("enter n of numbers"))
number = int(input("enter a number"))
greatest = number
smallest = number

while n>1:
    number = int(input("enter a number "))
    if number > greatest :
        greatest = number
    if number < smallest :
        smallest = number
    n = n-1
print(f"the greatest number is {greatest}")
print(f"the smallest number is {smallest}")