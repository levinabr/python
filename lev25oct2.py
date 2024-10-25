"""
Author -  Levin Abraham Jacob
date - 25/10/2024
description - Write a Python program to convert temperature values back and forth between
 Celsius and Fahrenheit.
The user should be able to input a temperature in Celsius or Fahrenheit,
and the program should convert it to the other unit using the formula:

"""
temp = int(input("enter the temperature\n"))
unit =input("the unit of temperature is ?(c)(f)\n")
if unit == "c" :
    f = (temp*9/5)+32
    print(f,"is the converted temperature")
if unit=="f":
        c= 9/5*(temp-32)
        print(c,"is the converted temperature")


