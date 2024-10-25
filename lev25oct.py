"""
date= 25-10-2024
Author - Levin Abraham Jacob
AIM: Write a Python program to find the largest of three numbers.
The program should take three numbers as input from the user and determine
which one is the largest. Use conditional statements to compare the numbers

"""
n1 = input("Enter first number \n")
n2 = input("enter second number \n")
n3 = input("Enter third number\n")
if n2<n1>n3 :
    print("the largest number is",n1)
elif n1<n2>n3 :
    print("the largest number is",n2)
else :
    print("the largest number is ",n3)


