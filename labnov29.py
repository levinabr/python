"""
date = 29 - 11- 2024
Description = Program to check whether the given number is a valid mobile number or not using functions
name = levin abraham jacob
"""

def number_valid(number):

    if len(number)==10 and number[0] in "987":
        return True
    return False
mobile_num = input("Enter a mobile number")
if number_valid(mobile_num):
    print(f"the mobile number {mobile_num} is valid")
else :
    print(f"the number {mobile_num} is invalid")
