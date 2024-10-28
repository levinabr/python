"""
Author = Levin Abraham Jacob
date = 28 / 10/2024
Description = Write a menu-driven Python program that allows users to convert temperatures
between Celsius and Fahrenheit.
The program should repeatedly display a menu with three options:

    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program

Based on the user's choice:

    If they select option 1, prompt them to enter a temperature in Celsius and
    display the equivalent temperature in Fahrenheit.
    If they select option 2, prompt them to enter a temperature in Fahrenheit and
    display the equivalent temperature in Celsius.
    If they select option 3, exit the program.


"""
while True :
    temp = int(input("Enter The Temperature\n"))
    print("c.\t Celsius  ")
    print("f.\tFahrenheit")
    print("e.\texit()")
    choice = (input("Enter Your Unit Of Temperature \n"))
    if choice =="c":
        f = (temp * 9 / 5) + 32
        print(f, "is the converted temperature\n")

    elif choice =="f":
        c = 5/9* (temp - 32)
        print(c, "is the converted temperature\n")

    elif choice =="e" :
        break
    else:
        print("Invalid Temperature")
